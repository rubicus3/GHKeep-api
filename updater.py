import datetime
from time import strftime, sleep
import requests


import db
from schemas import Temperature_Humidity
from constants import arduino_link

token = ''

def create():
    """
        Функция для добавления новых данных с датчиков в базу данных раз в n минут
    """
    time = strftime("%H:%M")
    global token
    if datetime.datetime.now().minute % 1 == 0:
        air_sensors = requests.get(f"{arduino_link}/get_air_stats").json()
        for i in air_sensors:
            temp_hum = Temperature_Humidity(**i)
            temp_hum.tim = time
            db.create_temp_hum(temperature_humidity=temp_hum)

        hum_sensors = requests.get(f"{arduino_link}/get_soil_stats").json()
        for j in hum_sensors:
            hum = Temperature_Humidity(**j)
            hum.tim = time
            db.create_hum(temperature_humidity=hum)


if __name__ == '__main__':
    while True:
        sleep(60)
        create()
