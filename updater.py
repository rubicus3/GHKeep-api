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
        for i in range(1, 5):
            request = requests.get(f"https://dt.miet.ru/ppo_it/api/temp_hum/{i}")
            temp_hum = Temperature_Humidity(**request.json())
            temp_hum.tim = tim
            db.create_temp_hum(temperature_humidity=temp_hum)
        for j in range(1, 7):
            request = requests.get(f"https://dt.miet.ru/ppo_it/api/hum/{j}")  # тестовая строка
            hum = Temperature_Humidity(**request.json())
            hum.tim = tim
            db.create_hum(temperature_humidity=hum)


if __name__ == '__main__':
    while True:
        time.sleep(60)
        create()