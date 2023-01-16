"""

    Модуль для работы с базой данных

"""
from typing import List
import mariadb
import sys
from schemas import Temperature_Humidity, Watering, Warnings


def wrapper():
    """

        Функция для подключения к базе данных

        Returns: коннектор к базе данных

    """
    try:
        conn = mariadb.connect(
            # user="mike",
            user="root",
            password="INT2201765",
            # password="jetflash",
            # password="testpass",
            host="127.0.0.1",
            port=3306,
            database="case_8"
        )
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    return conn


# ---------------------------------------------------- DB Create ----------------------------------------------------- #


def create_fork():
    """

        Функция для создания форточек

        :param kwargs: состояние форточек

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Create_fork();")
    conn.commit()
    conn.close()


def create_hum(**kwargs):
    """

        Функция для создания датчика влажности почвы

        :param kwargs: класс Temperature_Humidity с: id датчика и влажность почвы

    """
    conn = wrapper()
    cur = conn.cursor()
    a: Temperature_Humidity = kwargs['temperature_humidity']
    cur.execute("CALL Create_hum(?, ?)", (int(a.id), a.humidity))
    conn.commit()
    conn.close()


def create_temp_hum(**kwargs):
    """

        Функция для создания датчика температуры и влажности воздуха

        :param kwargs: класс Temperature_Humidity с: id датчика, температура и влажность воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    a: Temperature_Humidity = kwargs["temperature_humidity"]
    cur.execute("CALL Create_temp_hum(?, ?, ?)", (a.id, a.temperature, a.humidity))
    conn.commit()
    conn.close()


def create_total_hum():
    """

        Функция для создания единой системы увлажнения

        :param kwargs: состояние системы

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Create_total_hum();")
    conn.commit()
    conn.close()


def create_watering(**kwargs):
    """

        Функция для создания системы полива грядки

        :param kwargs: класс Watering с: id и состоянием системы

    """
    conn = wrapper()
    cur = conn.cursor()
    a = kwargs["id"]
    cur.execute("CALL Create_watering(?, ?)", (a,))
    conn.commit()
    conn.close()


def create_warnings():
    """

        Функция для создания порогов среднего значения значений

        :param kwargs: класс Warnings с: порогами средних значений температуры, влажности воздуха и почвы

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Create_warnings();")
    conn.commit()
    conn.close()


# ------------------------------------------------------ DB PUT ------------------------------------------------------ #


def change_fork():
    """

        Функция для изменения состояния форточек

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Change_fork();")
    conn.commit()
    conn.close()


def change_total_hum():
    """

        Функция для изменения состояния единой системы увлажнения

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Change_total_hum();")
    conn.commit()
    conn.close()


def change_watering(**kwargs):
    """

        Функция для изменения состояния одной из систем полива

        :param kwargs: id системы

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Change_watering(?)", (kwargs['id'],))
    conn.commit()
    conn.close()


def change_warnings_temp(**kwargs):
    """

        Функция для изменения порога среднего значения температуры

        :param kwargs: новый порог среднего значения температуры

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_temp(?)", (kwargs["temperature"],))
    conn.commit()
    conn.close()


def change_warnings_h(**kwargs):
    """

        Функция для изменения порога среднего значения влажности воздуха

        :param kwargs: новый порог среднего значения влажности воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_h(?)", (kwargs["humidity_air"],))
    conn.commit()
    conn.close()


def change_warnings_hb(**kwargs):
    """

        Функция для изменения порога среднего значения влажности почвы

        :param kwargs: новый порог среднего значения влажности почвы

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_hb(?)", (kwargs["humidity_soil"],))
    conn.commit()
    conn.close()


# ------------------------------------------------------ DB GET ------------------------------------------------------ #


def get_fork():
    """

        Функция для получения состояния системы форточек

        :return: состояние системы форточек (1 или 0)

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_fork();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def get_hum(**kwargs):
    """

        Функция для получения данных с датчика почвы

        :param kwargs: id датчика почвы

        :return: список с id датчика и значением влажности почвы

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_hum(?)", (kwargs["hum_id"],))
    a = []
    for p_id, humidity in cur:
        a.append(Temperature_Humidity(id=p_id, humidity=humidity))
    conn.close()
    return a


def get_temp_from_temp_hum():
    """

        Функция для получения всех значений температуры со всех датчиков воздуха для вычисления средней температуры

        :return: все значения температуры со всех датчиков воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_temp_from_temp_hum();")
    a = []
    for i in cur:
        for x in i:
            a.append(int(x))
    conn.close()
    return a


def get_hum_temp(**kwargs):
    """

        Функция для получения данных с датчика воздуха

        :param kwargs: id датчика воздуха

        :return: список с id датчик, значениями температуры и влажности воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_hum_temp(?)", (kwargs["id"],))
    a = []
    for p_id, temp, hum in cur:
        a.append(Temperature_Humidity(id=p_id, temperature=temp, humidity=hum))
    conn.close()
    return a


def get_hum_from_temp_hum():
    """

         Функция для получения всех значений влажности со всех датчиков воздуха для вычисления средней влажности

        :return: все значения влажности со всех датчиков воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_hum_from_temp_hum();")
    a = []
    for i in cur:
        for x in i:
            a.append(int(x))
    conn.close()
    return a


def get_total_hum():
    """
        Функция для получения состояния единой системы

        :return: состояние единой системы (1 или 0)

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_total_hum();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def get_warnings():
    """
    
        Функция для получения порогов средних значений
        
        :return: пороги средних значений температуры, влажности воздуха и влажности почвы
         
    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_warnings();")
    a = []
    for temp, hum, hd in cur:
        a.append(Warnings(temperature=temp, humidity_air=hum, humidity_soil=hd))
    conn.close()
    return a


def get_watering(**kwargs):
    """

        Функция для получения состояния системы полива

        :param kwargs: id системы полива

        :return: состояние системы полива

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_watering(?)", (kwargs["id"],))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat

