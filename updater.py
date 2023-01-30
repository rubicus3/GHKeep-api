import datetime
import time
import requests

import db
from schemas import Temperature_Humidity
import schedule

# import api
token = ''


def create():
    # api.create_hum()
    # api.create_temp_hum()
    tim = time.strftime("%H:%M")

    global token
    if datetime.datetime.now().minute % 5 == 0:
        for i in range(1, 5):
            # headers = {"X-Auth-Token": token}
            # request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}", headers=headers)
            request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}")  # тестовая строка
            temp_hum = Temperature_Humidity(**request.json())
            temp_hum.tim = tim
            db.create_temp_hum(temperature_humidity=temp_hum)
        for j in range(1, 7):
            # headers = {"X-Auth-Token": token}
            # request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{i}", headers=headers)
            request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{j}")  # тестовая строка
            hum = Temperature_Humidity(**request.json())
            hum.tim = tim
            db.create_hum(temperature_humidity=hum)


while True:

    time.sleep(60)
    create()