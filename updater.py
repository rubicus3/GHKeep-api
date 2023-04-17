import datetime
import time
import requests

import db
from schemas import Temperature_Humidity

token = ''


def create():
    """
        Функция для добавления новых данных с датчиков в базу данных раз в 5 минут
    """
    tim = time.strftime("%H:%M")
    global token
    if datetime.datetime.now().minute % 5 == 0:
        air_sensors = (requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}"))
        for i in air_sensors:
            temp_hum = i
            temp_hum.tim = tim
            db.create_temp_hum(temperature_humidity=temp_hum)
        hum_sensors = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{j}")
        for j in hum_sensors:
            hum = j
            hum.tim = tim
            db.create_hum(temperature_humidity=hum)


if __name__ == '__main__':
    while True:
        time.sleep(60)
        create()