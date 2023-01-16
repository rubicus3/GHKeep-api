# from datetime import timedelta, datetime, timezone
from typing import Optional

import uvicorn as uvicorn

import db
import requests
import fastapi
from fastapi.responses import JSONResponse
from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#
# from logic import registration_checker, name_checker, login_checker
from schemas import Temperature_Humidity, List_Temperature_Humidity, Warnings, Watering, Fork

app = fastapi.FastAPI()

token = "" # нужно вставить токен


# ----------------------------------------------------- API POST ----------------------------------------------------- #


@app.post("/create_fork", status_code=201)
def create_fork():
    db.create_fork()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created fork")


@app.post("/create_hum", status_code=201)
def create_hum():
    global token
    for i in range(1, 7):
        # headers = {"X-Auth-Token": token}
        # request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{i}", headers=headers)
        request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{i}") # тестовая строка
        hum = Temperature_Humidity(**request.json())
        db.create_hum(temperature_humidity=hum)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created hums")


@app.post("/create_temp_hum", status_code=201)
def create_temp_hum():
    global token
    for i in range(1, 5):
        # headers = {"X-Auth-Token": token}
        # request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}", headers=headers)
        request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}") # тестовая строка
        temp_hum = Temperature_Humidity(**request.json())
        db.create_temp_hum(temperature_humidity=temp_hum)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created temp_hums")


@app.post("/create_total_hum", status_code=201)
def create_total_hum():
    db.create_total_hum()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created total_hum")


@app.post("/create_watering", status_code=201)
def create_watering():
    for i in range(1, 7):
        db.create_watering(id=i)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created waterings")


@app.post("/create_warnings", status_code=201)
def create_warnings():
    db.create_warnings()
    return JSONResponse(status_code=status.HTTP_201_CREATED, content="Created warnings")


# ----------------------------------------------------- API PUT ----------------------------------------------------- #


@app.put("/change_fork", status_code=200)
def change_fork():
    db.change_fork()
    return JSONResponse(status_code=status.HTTP_200_OK, content="Changed fork")


# ----------------------------------------------------- API GET ----------------------------------------------------- #


@app.get("/get_hum/{id}")
def get_hum(ids: int):
    return List_Temperature_Humidity(temp_hums=db.get_hum(hum_id=ids))


if __name__ == '__main__':
    uvicorn.run("api:app", host="127.0.0.1", port=8000)