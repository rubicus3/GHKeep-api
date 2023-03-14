"""

    Модуль для взаимодействия между фронтендом и бэкендом

"""

import subprocess
import uvicorn

import db
import requests
import fastapi
from fastapi.responses import JSONResponse
from fastapi import status
from schemas import Average_List, T_H_List, Soil_Warnings

app = fastapi.FastAPI()

token = ""  # нужно вставить токен


# ----------------------------------------------------- API PUT ----------------------------------------------------- #


@app.put("/change_fork_state/{extra}", status_code=200)
def change_fork_state(extra: bool):
    global token
    if db.get_fork():
        db.change_fork()
        state = db.get_fork()
        # headers = {"X-Auth-Token": token}
        requests.patch(f"https://dt.miet.ru/ppo_it/api/fork_drive?state={state}")
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")
    else:
        if not extra:
            sensor_states = db.get_temp_from_temp_hum()[-4::]
            num = 0
            for i in sensor_states:
                num += i.temperature
            num /= 4
            warnings = db.get_warnings()
            if float(num) > float(warnings.temperature):
                db.change_fork()
                state = db.get_fork()
                # headers = {"X-Auth-Token": token}
                requests.patch(f"https://dt.miet.ru/ppo_it/api/fork_drive?state={state}")
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="The average temperature did not exceed the permissible value")
        else:
            db.change_fork()
            state = db.get_fork()
            # headers = {"X-Auth-Token": token}
            requests.patch(f"https://dt.miet.ru/ppo_it/api/fork_drive?state={state}")
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")


@app.put("/change_total_hum_state/{extra}", status_code=200)
def change_total_hum_state(extra: bool):
    global token
    if db.get_total_hum():
        db.change_total_hum()
        state = db.get_total_hum()
        # headers = {"X-Auth-Token": token}
        requests.patch(f"https://dt.miet.ru/ppo_it/api/total_hum?state={state}")
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")
    else:
        if not extra:
            sensor_states = db.get_hum_from_temp_hum()[-4::]
            num = 0
            for i in sensor_states:
                num += i.humidity
            num /= 4
            warnings = db.get_warnings()
            if float(num) < float(warnings.humidity_air):
                db.change_total_hum()
                state = db.get_total_hum()
                # headers = {"X-Auth-Token": token}
                requests.patch(f"https://dt.miet.ru/ppo_it/api/total_hum?state={state}")
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="The average humidity did not fall below the permissible value")
        else:
            db.change_total_hum()
            state = db.get_total_hum()
            # headers = {"X-Auth-Token": token}
            requests.patch(f"https://dt.miet.ru/ppo_it/api/total_hum?state={state}")
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")


@app.put("/change_watering_system_state/{id}/{extra}", status_code=200)
def change_watering_system_state(id: int, extra: bool):
    global token
    if db.get_watering(id=id):
        db.change_watering(id=id)
        state = db.get_watering(id=id)
        # headers = {"X-Auth-Token": token}
        requests.patch(f"https://dt.miet.ru/ppo_it/api/watering?id={id}&state={state}")
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")
    else:
        if not extra:
            sensors_states = db.get_hum_for_table()
            sensor_states = sensors_states[id-1]
            warnings = db.get_soil_warnings(id=id)
            if float(sensor_states) < float(warnings.hb):
                db.change_watering(id=id)
                state = db.get_watering(id=id)
                # headers = {"X-Auth-Token": token}
                requests.patch(f"https://dt.miet.ru/ppo_it/api/watering?id={id}&state={state}")
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="The Hb did not fall below the permissible value")
        else:
            db.change_watering(id=id)
            state = db.get_watering(id=id)
            # headers = {"X-Auth-Token": token}
            requests.patch(f"https://dt.miet.ru/ppo_it/api/watering?id={id}&state={state}")
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")


@app.put("/change_temperature_warnings/{temperature}", status_code=200)
def change_temperature_warnings(temperature: float):
    if temperature < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if temperature > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_temp(temperature=temperature)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_temp")


@app.put("/change_humidity_air_warnings/{humidity_air}", status_code=200)
def change_humidity_air_warnings(humidity_air: float):
    if humidity_air < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if humidity_air > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_h(humidity_air=humidity_air)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_h")


@app.put("/change_humidity_soil_warnings/{id}/{humidity_soil}", status_code=200)
def change_humidity_soil_warnings(id: int, humidity_soil: float):
    if humidity_soil < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if humidity_soil > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_hb(soil_warn=Soil_Warnings(id=id, hb=humidity_soil))
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_hb")


# ----------------------------------------------------- API GET ----------------------------------------------------- #


@app.get("/get_humidity_air_temperature_for_table")
def get_humidity_air_temperature_for_table():
    return db.get_temp_hum_for_table()


@app.get("/get_humidity_soil_for_table")
def get_humidity_soil_for_table():
    return T_H_List(h_list=db.get_hum_for_table())


@app.get("/get_humidity_air_temperature_for_graphics")
def get_humidity_air_temperature_for_graphics():
    sensors_states = []
    for i in range(1, 5):
        states = db.get_hum_temp(id=i)
        states_list = T_H_List(id=i, t_list=[], h_list=[], tim_list=[])
        for j in states:
            states_list.t_list.append(j.temperature)
            states_list.h_list.append(j.humidity)
            states_list.tim_list.append(j.tim)
        sensors_states.append(states_list)
    return sensors_states


@app.get("/get_humidity_soil_for_graphics")
def get_humidity_soil_for_graphics():
    sensors_states = []
    for i in range(1, 7):
        states = db.get_hum(hum_id=i)
        states_list = T_H_List(id=i, h_list=[], tim_list=[])
        for j in states:
            states_list.h_list.append(j.humidity)
            states_list.tim_list.append(j.tim)
        sensors_states.append(states_list)
    return sensors_states


@app.get("/get_average_temperature")
def get_average_temperature():
    """

        Функция для получения средней температуры

        :return: список со значениями средней температуры

    """
    sensors_states = db.get_temp_from_temp_hum()
    temperature = 0
    average_states_list = Average_List(d_list=[], t_list=[])
    num = 0 # счетчик
    average_state_time = ''
    for i in sensors_states:
        if num < 4:
            temperature += i.temperature
            num += 1
            average_state_time = i.tim
        if num == 4:
            average_states_list.d_list.append(round((temperature/4), 2))
            average_states_list.t_list.append(average_state_time)
            num = 0
            temperature = 0

    return average_states_list


@app.get("/get_average_humidity")
def get_average_humidity():
    """

        Функция для получения средней влажности воздуха

        :return: список со значениями средней влажности воздуха

    """
    sensors_states = db.get_hum_from_temp_hum()
    humidity = 0
    average_states_list = Average_List(d_list=[], t_list=[])
    num = 0
    average_state_time = ''
    for i in sensors_states:
        if num < 4:
            humidity += i.humidity
            num += 1
            average_state_time = i.tim
        if num == 4:
            average_states_list.d_list.append(round((humidity/4), 2))
            average_states_list.t_list.append(average_state_time)
            num = 0
            humidity = 0
    return average_states_list


@app.get("/get_fork_state")
def get_fork_state():
    return db.get_fork()


@app.get("/get_total_hum_state")
def get_total_hum_state():
    return db.get_total_hum()


@app.get("/get_watering_system_state/{id}")
def get_watering_system_state(id: int):
    return db.get_watering(id=id)


@app.get("/get_warnings_states")
def get_warnings_states():
    air_warnings = db.get_warnings()
    soil_warnings = []
    for i in range(1, 7):
        soil_warnings.append(db.get_soil_warnings(id=i))
    return {"temperature": air_warnings.temperature,
            "humidity_air": air_warnings.humidity_air,
            "humidity_soil": soil_warnings}


if __name__ == '__main__':
    subprocess.Popen(["python3", "updater.py"])
    uvicorn.run("api:app", host="0.0.0.0", port=8000)
