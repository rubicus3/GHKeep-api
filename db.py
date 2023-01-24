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
            user="root",
            password="INT2201765",
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
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Create_fork();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def create_hum(**kwargs):
    """

        Функция для создания датчика влажности почвы

        :param kwargs: класс Temperature_Humidity с: id датчика и влажность почвы

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    a: Temperature_Humidity = kwargs['temperature_humidity']
    cur.execute("CALL Create_hum(?, ?, ?)", (int(a.id), a.humidity, a.tim))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def create_temp_hum(**kwargs):
    """

        Функция для создания датчика температуры и влажности воздуха

        :param kwargs: класс Temperature_Humidity с: id датчика, температура и влажность воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    conn.autocommit = True
    a: Temperature_Humidity = kwargs["temperature_humidity"]
    cur.execute("CALL Create_temp_hum(?, ?, ?, ?)", (a.id, a.temperature, a.humidity, a.tim))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def create_total_hum():
    """

        Функция для создания единой системы увлажнения

        :param kwargs: состояние системы

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Create_total_hum();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def create_waterings():
    for i in range(1, 7):
        create_watering(id=i)


def create_watering(**kwargs):
    """

        Функция для создания системы полива грядки

        :param kwargs: класс Watering с: id и состоянием системы

    """
    conn = wrapper()
    cur = conn.cursor()
    conn.autocommit = True
    a = kwargs["id"]
    cur.execute("CALL Create_watering(?)", (a,))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def create_warnings():
    """

        Функция для создания порогов среднего значения значений

        :param kwargs: класс Warnings с: порогами средних значений температуры, влажности воздуха и почвы

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Create_warnings();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


# ------------------------------------------------------ DB PUT ------------------------------------------------------ #


def change_fork():
    """

        Функция для изменения состояния форточек

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_fork();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def change_total_hum():
    """

        Функция для изменения состояния единой системы увлажнения

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_total_hum();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def change_watering(**kwargs):
    """

        Функция для изменения состояния одной из систем полива

        :param kwargs: id системы

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_watering(?)", (kwargs['id'],))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def change_warnings_temp(**kwargs):
    """

        Функция для изменения порога среднего значения температуры

        :param kwargs: новый порог среднего значения температуры

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_temp(?)", (kwargs["temperature"],))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def change_warnings_h(**kwargs):
    """

        Функция для изменения порога среднего значения влажности воздуха

        :param kwargs: новый порог среднего значения влажности воздуха

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_h(?)", (kwargs["humidity_air"],))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def change_warnings_hb(**kwargs):
    """

        Функция для изменения порога среднего значения влажности почвы

        :param kwargs: новый порог среднего значения влажности почвы

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_hb(?)", (kwargs["humidity_soil"],))
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


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
    for a_id, p_id, humidity, tim in cur:
        a.append(Temperature_Humidity(id=p_id, humidity=humidity, tim=tim))
    conn.close()
    return a[::-1]


def get_temp_from_temp_hum():
    """

        Функция для получения всех значений температуры со всех датчиков воздуха для вычисления средней температуры

        :return: все значения температуры со всех датчиков воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_temp_from_temp_hum();")
    a = []
    for a_id, i, t in cur:
        a.append(Temperature_Humidity(temperature=i, tim=t))
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
    for a_id, p_id, temp, hum, tim in cur:
        a.append(Temperature_Humidity(id=p_id, temperature=temp, humidity=hum, tim=tim))
    conn.close()
    return a[::-1]


def get_hum_from_temp_hum():
    """

         Функция для получения всех значений влажности со всех датчиков воздуха для вычисления средней влажности

        :return: все значения влажности со всех датчиков воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_hum_from_temp_hum();")
    a = []
    for a_id, i, t in cur:
        a.append(Temperature_Humidity(humidity=i, tim=t))
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
    a = ''
    for temp, hum, hd in cur:
        a = Warnings(temperature=temp, humidity_air=hum, humidity_soil=hd)
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

