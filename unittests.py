import time

import requests

import db
from schemas import Temperature_Humidity, Warnings, Soil_Warnings


# ------------------------------------------------------Get py-tests----------------------------------------------------#


def test_get_air_states():
    ls = []
    gt = []
    tim = time.strftime("%H:%M")
    for i in range(1, 5):
        request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}")
        temp_hum = Temperature_Humidity(**request.json())
        temp_hum.tim = tim
        db.create_temp_hum(temperature_humidity=temp_hum)
        ls.append(temp_hum)
    for i in range(1, 5):
        q = db.get_hum_temp(id=i)[-1]
        gt.append(q)
    assert ls == gt


def test_get_soil_states():
    ls = []
    gt = []
    tim = time.strftime("%H:%M")
    for j in range(1, 7):
        request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{j}")  # тестовая строка
        hum = Temperature_Humidity(**request.json())
        hum.tim = tim
        db.create_hum(temperature_humidity=hum)
        ls.append(hum)
    for j in range(1, 7):
        q = db.get_hum_soil(hum_id=j)[-1]
        gt.append(q)
    assert ls == gt


def test_change_fork_state():
    st = 1 - db.get_fork()
    db.change_fork_state()
    assert st == db.get_fork()


def test_change_total_hum_state():
    st = 1 - db.get_total_hum()
    db.change_total_hum_state()
    assert st == db.get_total_hum()


def test_change_watering_state():
    st = 1 - db.get_watering(id=1)
    db.change_watering_state(id=1)
    assert st == db.get_watering(id=1)


def test_change_air_warnings():
    db.change_warnings_temperature(temperature=25)
    db.change_warnings_humidity_air(humidity_air=68)
    assert db.get_warnings() == Warnings(temperature=25, humidity_air=68)


def test_change_warnings_soil():
    db.change_warnings_humidity_soil(soil_warn=Soil_Warnings(id=1, hb=73))
    assert Soil_Warnings(id=1, hb=73) == db.get_soil_warnings(id=1)
