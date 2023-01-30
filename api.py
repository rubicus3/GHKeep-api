import os
import subprocess
from typing import Optional
import time
import uvicorn as uvicorn

import db
import requests
import fastapi
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status
from schemas import Temperature_Humidity, List_Temperature_Humidity, Warnings, Watering, Average_List, T_H_List

app = fastapi.FastAPI()

token = ""  # нужно вставить токен


# ----------------------------------------------------- API POST ----------------------------------------------------- #


@app.post("/create_hum", status_code=201)
def create_hum():
    tim = time.strftime("%H:%M")
    global token
    for i in range(1, 7):
        # headers = {"X-Auth-Token": token}
        # request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{i}", headers=headers)
        request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{i}")  # тестовая строка
        hum = Temperature_Humidity(**request.json())
        hum.tim = tim
        db.create_hum(temperature_humidity=hum)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created hums")


@app.post("/create_temp_hum", status_code=201)
def create_temp_hum():
    tim = time.strftime("%H:%M")
    global token
    for i in range(1, 5):
        # headers = {"X-Auth-Token": token}
        # request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}", headers=headers)
        request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}")  # тестовая строка
        temp_hum = Temperature_Humidity(**request.json())
        temp_hum.tim = tim
        db.create_temp_hum(temperature_humidity=temp_hum)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created temp_hums")


# ----------------------------------------------------- API PUT ----------------------------------------------------- #


@app.put("/change_fork", status_code=200)
def change_fork():
    db.change_fork()
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")


@app.put("/change_total_hum", status_code=200)
def change_total_hum():
    db.change_total_hum()
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")


@app.put("/change_watering/{id}", status_code=200)
def change_watering(id: int):
    db.change_watering(id=id)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")


@app.put("/change_warnings_temp/{temperature}", status_code=200)
def change_warnings_temp(temp: float):
    db.change_warnings_temp(temperature=temp)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_temp")


@app.put("/change_warnings_h/{humidity_air}", status_code=200)
def change_warnings_h(hum: float):
    db.change_warnings_h(humidity_air=hum)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_h")


@app.put("/change_warnings_hb/{humidity_soil}", status_code=200)
def change_warnings_hb(hum: float):
    db.change_warnings_hb(humidity_soil=hum)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_hb")


# ----------------------------------------------------- API GET ----------------------------------------------------- #


@app.get("/get_fork")
def get_fork():
    return db.get_fork()


@app.get("/get_hum_for_table")
def get_hum_for_table():
    return T_H_List(h_list=db.get_hum_for_table())


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


@app.get("/get_hum_temp_for_table/{id}")
def get_hum_temp_for_table():
    return db.get_temp_hum_for_table()


@app.get("/get_total_hum")
def get_total_hum():
    return db.get_total_hum()


@app.get("/get_warnings")
def get_warnings():
    return db.get_warnings()


@app.get("/get_watering/{id}")
def get_watering(id: int):
    return db.get_watering(id=id)


@app.get("/get_temp_hum_for_graphics")
def get_temp_hum_for_graphics():
    q = []
    for i in range(1, 5):
        a = db.get_hum_temp(id=i)[::-1]
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
        a = db.get_hum(hum_id=i)[::-1]
        w = T_H_List(id=i, h_list=[], tim_list=[])
        for j in a:
            w.h_list.append(j.humidity)
            w.tim_list.append(j.tim)
        q.append(w)
    return q


if __name__ == '__main__':
    subprocess.Popen(["python3", "updater.py"])
    uvicorn.run("api:app", host="127.0.0.1", port=8000)
