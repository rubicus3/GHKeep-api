"""

    Модуль для взаимодействия между фронтендом и бэкендом

"""

import subprocess
import uvicorn
import time

import arduino_connect
import db
import fastapi
from fastapi.responses import JSONResponse
from fastapi import status
from schemas import Average_List, T_H_List, Soil_Warnings

app = fastapi.FastAPI()


# ----------------------------------------------------- API PUT ----------------------------------------------------- #


@app.put("/change_fork_state/{extra}", status_code=200)
def change_fork_state(extra: bool):
    """

            Функция для изменения состояния форточек

    """
    if db.get_fork():
        db.change_fork_state()
        state = db.get_fork()
        arduino_connect.change_fork_state(state)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")
    else:
        if not extra:
            st = db.get_temp_hum_num()
            sensor_states = db.get_temp_from_temp_hum()[-st::]
            num = 0
            for i in sensor_states:
                num += i.temperature
            num /= st
            warnings = db.get_warnings()
            if float(num) > float(warnings.temperature):
                db.change_fork_state()
                state = db.get_fork()
                arduino_connect.change_fork_state(state)
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                content="The average temperature did not exceed the permissible value"
                                )
        else:
            db.change_fork_state()
            state = db.get_fork()
            arduino_connect.change_fork_state(state)
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")


@app.put("/change_total_hum_state/{extra}", status_code=200)
def change_total_hum_state(extra: bool):
    """

            Функция для изменения состояния единой системы увлажнения

    """
    if db.get_total_hum():
        db.change_total_hum_state()
        state = db.get_total_hum()
        arduino_connect.change_total_hum_state(state)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")
    else:
        if not extra:
            st = db.get_temp_hum_num()
            sensor_states = db.get_hum_from_temp_hum()[-st::]
            num = 0
            for i in sensor_states:
                num += i.humidity
            num /= st
            warnings = db.get_warnings()
            if float(num) < float(warnings.humidity_air):
                db.change_total_hum_state()
                state = db.get_total_hum()
                arduino_connect.change_total_hum_state(state)
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                content="The average humidity did not fall below the permissible value"
                                )
        else:
            db.change_total_hum_state()
            state = db.get_total_hum()
            arduino_connect.change_total_hum_state(state)
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed total_hum")


@app.put("/change_watering_system_state/{id}/{extra}", status_code=200)
def change_watering_system_state(id: int, extra: bool):
    """

            Функция для изменения состояния одной из систем полива

    """
    if db.get_watering(id=id):
        db.change_watering_state(id=id)
        state = db.get_watering(id=id)
        arduino_connect.change_watering_system(state)
        time.sleep(5)
        db.change_watering_state(id=id)
        state = db.get_watering(id=id)
        arduino_connect.change_watering_system(state)
        return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")
    else:
        if not extra:
            sensors_states = db.get_hum_for_table()
            sensor_states = sensors_states[id-1]
            warnings = db.get_soil_warnings(id=id)
            if float(sensor_states) < float(warnings.hb):
                db.change_watering_state(id=id)
                state = db.get_watering(id=id)
                arduino_connect.change_watering_system(state)
                time.sleep(5)
                db.change_watering_state(id=id)
                state = db.get_watering(id=id)
                arduino_connect.change_watering_system(state)
                return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                                content="The Hb did not fall below the permissible value"
                                )
        else:
            db.change_watering_state(id=id)
            state = db.get_watering(id=id)
            arduino_connect.change_watering_system(state)
            time.sleep(5)
            db.change_watering_state(id=id)
            state = db.get_watering(id=id)
            arduino_connect.change_watering_system(state)
            return JSONResponse(status_code=status.HTTP_200_OK, content="Changed watering")


@app.put("/change_temperature_warnings/{temperature}", status_code=200)
def change_temperature_warnings(temperature: float):
    """

            Функция для изменения порога среднего значения температуры

    """
    if temperature < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if temperature > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_temperature(temperature=temperature)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_temp")


@app.put("/change_humidity_air_warnings/{humidity_air}", status_code=200)
def change_humidity_air_warnings(humidity_air: float):
    """

            Функция для изменения порога среднего значения влажности воздуха

    """
    if humidity_air < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if humidity_air > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_humidity_air(humidity_air=humidity_air)
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_h")


@app.put("/change_humidity_soil_warnings/{id}/{humidity_soil}", status_code=200)
def change_humidity_soil_warnings(id: int, humidity_soil: float):
    """

            Функция для изменения порога среднего значения влажности почвы

    """
    if humidity_soil < 0:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is less than allowed values")
    if humidity_soil > 100:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="Value is greater than allowed values")
    else:
        db.change_warnings_humidity_soil(soil_warn=Soil_Warnings(id=id, hb=humidity_soil))
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed warnings_hb")


# ----------------------------------------------------- API GET ----------------------------------------------------- #


@app.get("/get_humidity_air_temperature_for_table")
def get_humidity_air_temperature_for_table():
    """

            Функция для получения последних данных о воздухе для таблицы

    """
    return db.get_temp_hum_for_table()


@app.get("/get_humidity_soil_for_table")
def get_humidity_soil_for_table():
    """

            Функция для получения последних данных о почве для таблицы

    """
    return T_H_List(h_list=db.get_hum_for_table())


@app.get("/get_humidity_air_temperature_for_graphics")
def get_humidity_air_temperature_for_graphics():
    """

            Функция для получения данных с датчиков воздуха для графиков

    """
    sensors_states = []
    st = db.get_temp_hum_num()
    for i in range(1, st + 1):
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
    """

                Функция для получения данных с датчиков почвы для графиков

    """
    sensors_states = []
    st = db.get_hum_num()
    for i in range(1, st + 1):
        states = db.get_hum_soil(hum_id=i)
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
    num = 0  # счетчик
    average_state_time = ''
    s = len(sensors_states) // 5
    for i in sensors_states:
        if num < s:
            temperature += i.temperature
            num += 1
            average_state_time = i.tim
        if num == s:
            average_states_list.d_list.append(round((temperature / s), 2))
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
    s = len(sensors_states) // 5
    for i in sensors_states:
        if num < s:
            humidity += i.humidity
            num += 1
            average_state_time = i.tim
        if num == s:
            average_states_list.d_list.append(round((humidity / s), 2))
            average_states_list.t_list.append(average_state_time)
            num = 0
            humidity = 0
    return average_states_list


@app.get("/get_fork_state")
def get_fork_state():
    """

            Функция для получения состояния системы форточек

    """
    return db.get_fork()


@app.get("/get_total_hum_state")
def get_total_hum_state():
    """
            Функция для получения состояния единой системы

    """
    return db.get_total_hum()


@app.get("/get_watering_system_state/{id}")
def get_watering_system_state(id: int):
    """

            Функция для получения состояния системы полива

    """
    return db.get_watering(id=id)


@app.get("/get_warnings_states")
def get_warnings_states():
    """

            Функция для получения порогов средних значений

    """
    air_warnings = db.get_warnings()
    soil_warnings = []
    st = db.get_hum_num()
    for i in range(1, st + 1):
        soil_warnings.append(db.get_soil_warnings(id=i))
    return {"temperature": air_warnings.temperature,
            "humidity_air": air_warnings.humidity_air,
            "humidity_soil": soil_warnings}


if __name__ == '__main__':
    subprocess.Popen(["python3", "updater.py"])
    uvicorn.run("api:app", host="0.0.0.0", port=8000)
