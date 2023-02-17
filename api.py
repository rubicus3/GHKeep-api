import subprocess
import time
import uvicorn as uvicorn

import db
import requests
import fastapi
from fastapi.responses import JSONResponse
from fastapi import status
from schemas import Temperature_Humidity, Average_List, T_H_List, Soil_Warnings

app = fastapi.FastAPI()

token = ""  # нужно вставить токен


# ----------------------------------------------------- API POST ----------------------------------------------------- #

#
# @app.post("/create_hum", status_code=201)
# def create_hum():
#     tim = time.strftime("%H:%M")
#     global token
#     for i in range(1, 7):
#         # headers = {"X-Auth-Token": token}
#         # request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{i}", headers=headers)
#         request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{i}")  # тестовая строка
#         hum = Temperature_Humidity(**request.json())
#         hum.tim = tim
#         db.create_hum(temperature_humidity=hum)
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created hums")
#
#
# @app.post("/create_temp_hum", status_code=201)
# def create_temp_hum():
#     tim = time.strftime("%H:%M")
#     global token
#     for i in range(1, 5):
#         # headers = {"X-Auth-Token": token}
#         # request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}", headers=headers)
#         request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}")  # тестовая строка
#         temp_hum = Temperature_Humidity(**request.json())
#         temp_hum.tim = tim
#         db.create_temp_hum(temperature_humidity=temp_hum)
#     return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created temp_hums")


# ----------------------------------------------------- API PUT ----------------------------------------------------- #


@app.put("/change_fork/{extra}", status_code=200)
def change_fork(extra: bool):
    global token
    if db.get_fork():
        db.change_fork()
        q = db.get_fork()
        headers = {"X-Auth-Token": token}
        requests.patch("https://dt.miet.ru/ppo_it/api/fork_drive/ ", {"state": q}, headers=headers)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")
    else:
        if not extra:
            a = db.get_temp_from_temp_hum()[-4::]
            e = 0
            for i in a:
                e += i.temperature
            e /= 4
            w = db.get_warnings()
            if float(e) > float(w.temperature):
                db.change_fork()
                q = db.get_fork()
                headers = {"X-Auth-Token": token}
                requests.patch("https://dt.miet.ru/ppo_it/api/fork_drive/ ", {"state": q}, headers=headers)
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="The average temperature did not exceed the permissible value")
        else:
            db.change_fork()
            q = db.get_fork()
            headers = {"X-Auth-Token": token}
            requests.patch("https://dt.miet.ru/ppo_it/api/fork_drive/ ", {"state": q}, headers=headers)
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")


@app.put("/change_total_hum/{extra}", status_code=200)
def change_total_hum(extra: bool):
    global token
    if db.get_total_hum():
        db.change_total_hum()
        q = db.get_total_hum()
        headers = {"X-Auth-Token": token}
        requests.patch("https://dt.miet.ru/ppo_it/api/total_hum", {"state": q}, headers=headers)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")
    else:
        if not extra:
            a = db.get_hum_from_temp_hum()[-4::]
            e = 0
            for i in a:
                e += i.humidity
            e /= 4
            w = db.get_warnings()
            if float(e) < float(w.humidity_air):
                db.change_total_hum()
                q = db.get_total_hum()
                headers = {"X-Auth-Token": token}
                requests.patch("https://dt.miet.ru/ppo_it/api/total_hum", {"state": q}, headers=headers)
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="The average humidity did not fall below the permissible value")
        else:
            db.change_total_hum()
            q = db.get_total_hum()
            headers = {"X-Auth-Token": token}
            requests.patch("https://dt.miet.ru/ppo_it/api/total_hum", {"state": q}, headers=headers)
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")


@app.put("/change_watering/{id}/{extra}", status_code=200)
def change_watering(id: int, extra: bool):
    global token
    if db.get_watering(id=id):
        db.change_watering(id=id)
        q = db.get_watering(id=id)
        headers = {"X-Auth-Token": token}
        requests.patch("https://dt.miet.ru/ppo_it/api/watering", {"id": id, "state": q}, headers=headers)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")
    else:
        if not extra:
            a = db.get_hum_for_table()
            w = a[id-1]
            e = db.get_soil_warnings(id=id)
            if float(w) < float(e.hb):
                db.change_watering(id=id)
                q = db.get_watering(id=id)
                headers = {"X-Auth-Token": token}
                requests.patch("https://dt.miet.ru/ppo_it/api/watering", {"id": id, "state": q}, headers=headers)
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="The Hb did not fall below the permissible value")
        else:
            db.change_watering(id=id)
            q = db.get_watering(id=id)
            headers = {"X-Auth-Token": token}
            requests.patch("https://dt.miet.ru/ppo_it/api/watering", {"id": id, "state": q}, headers=headers)
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")


@app.put("/change_warnings_temp/{temperature}", status_code=200)
def change_warnings_temp(temperature: float):
    if temperature < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if temperature > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_temp(temperature=temperature)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_temp")


@app.put("/change_warnings_h/{humidity_air}", status_code=200)
def change_warnings_h(humidity_air: float):
    if humidity_air < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if humidity_air > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_h(humidity_air=humidity_air)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_h")


@app.put("/change_warnings_hb/{id}/{humidity_soil}", status_code=200)
def change_warnings_hb(id: int, humidity_soil: float):
    if humidity_soil < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if humidity_soil > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_hb(soil_warn=Soil_Warnings(id=id, hb=humidity_soil))
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_hb")


# ----------------------------------------------------- API GET ----------------------------------------------------- #


@app.get("/get_hum_temp_for_table")
def get_hum_temp_for_table():
    return db.get_temp_hum_for_table()


@app.get("/get_hum_for_table")
def get_hum_for_table():
    return T_H_List(h_list=db.get_hum_for_table())


@app.get("/get_temp_hum_for_graphics")
def get_temp_hum_for_graphics():
    q = []
    for i in range(1, 5):
        a = db.get_hum_temp(id=i)
        w = T_H_List(id=i, t_list=[], h_list=[], tim_list=[])
        for j in a:
            w.t_list.append(j.temperature)
            w.h_list.append(j.humidity)
            w.tim_list.append(j.tim)
        q.append(w)
    return q


@app.get("/get_hum_for_graphics")
def get_hum_for_graphics():
    q = []
    for i in range(1, 7):
        a = db.get_hum(hum_id=i)
        w = T_H_List(id=i, h_list=[], tim_list=[])
        for j in a:
            w.h_list.append(j.humidity)
            w.tim_list.append(j.tim)
        q.append(w)
    return q


@app.get("/get_average_temperature")
def get_average_temperature():
    """

        Функция для получения средней температуры

        :return: список со значениями средней температуры

    """
    a = db.get_temp_from_temp_hum()
    t = 0
    q = Average_List(d_list=[], t_list=[])
    e = 0
    w = ''
    for i in a:
        if e < 4:
            t += i.temperature
            e += 1
            w = i.tim
        if e == 4:
            q.d_list.append(round((t/4), 2))
            q.t_list.append(w)
            e = 0
            t = 0

    return q


@app.get("/get_average_humidity")
def get_average_humidity():
    """

        Функция для получения средней влажности воздуха

        :return: список со значениями средней влажности воздуха

    """
    a = db.get_hum_from_temp_hum()
    t = 0
    q = Average_List(d_list=[], t_list=[])
    e = 0
    w = ''
    for i in a:
        if e < 4:
            t += i.humidity
            e += 1
            w = i.tim
        if e == 4:
            q.d_list.append(round((t/4), 2))
            q.t_list.append(w)
            e = 0
            t = 0
    return q


@app.get("/get_fork")
def get_fork():
    return db.get_fork()


@app.get("/get_total_hum")
def get_total_hum():
    return db.get_total_hum()


@app.get("/get_watering/{id}")
def get_watering(id: int):
    return db.get_watering(id=id)


@app.get("/get_warnings")
def get_warnings():
    q = db.get_warnings()
    w = []
    for i in range(1, 7):
        w.append(db.get_soil_warnings(id=i))
    return {"temperature": q.temperature,
            "humidity_air": q.humidity_air,
            "humidity_soil": w}


# @app.get("/get_soil_warnings/{id}")
# def get_soil_warnings(id: int):
#     return db.get_soil_warnings(id=id)


if __name__ == '__main__':
    subprocess.Popen(["python3", "updater.py"])
    uvicorn.run("api:app", host="0.0.0.0", port=8000)
