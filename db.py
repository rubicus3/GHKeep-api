"""

    Модуль для работы с базой данных

"""
import mariadb
import sys
from schemas import Temperature_Humidity, Warnings, T_H_List, Soil_Warnings
from constants import mariadb_password

def wrapper():
    """

        Функция для подключения к базе данных

        Returns: коннектор к базе данных

    """
    try:
        conn = mariadb.connect(
            user="root",
            password=mariadb_password,
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

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Create_fork();")
    conn.close()


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
    conn.close()


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
    conn.close()


def create_total_hum():
    """

        Функция для создания единой системы увлажнения

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Create_total_hum();")
    conn.close()


def create_waterings():
    st = get_hum_num()
    for i in range(1, st + 1):
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
    conn.close()


# ------------------------------------------------------ DB PUT ------------------------------------------------------ #


def change_fork_state():
    """

        Функция для изменения состояния форточек

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_fork();")
    conn.close()


def change_total_hum_state():
    """

        Функция для изменения состояния единой системы увлажнения

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_total_hum();")
    conn.close()


def change_watering_state(**kwargs):
    """

        Функция для изменения состояния одной из систем полива

        :param kwargs: id системы

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_watering(?)", (kwargs['id'],))
    conn.close()


def change_warnings_temperature(**kwargs):
    """

        Функция для изменения порога среднего значения температуры

        :param kwargs: новый порог среднего значения температуры

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_temp(?)", (kwargs["temperature"],))
    conn.close()


def change_warnings_humidity_air(**kwargs):
    """

        Функция для изменения порога среднего значения влажности воздуха

        :param kwargs: новый порог среднего значения влажности воздуха

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("CALL Change_warnings_h(?)", (kwargs["humidity_air"],))
    conn.close()


def change_warnings_humidity_soil(**kwargs):
    """

        Функция для изменения порога среднего значения влажности почвы

        :param kwargs: новый порог среднего значения влажности почвы

    """
    conn = wrapper()
    conn.autocommit = True
    cur = conn.cursor()
    a: Soil_Warnings = kwargs['soil_warn']
    cur.execute("CALL Change_warnings_hb(?,? )", (a.id, a.hb))
    conn.close()


# ------------------------------------------------------ DB GET ------------------------------------------------------ #


def get_temp_hum_num():
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_temp_hum_num();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def get_hum_num():
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_hum_num();")
    stat = ''
    for i in cur:
        for x in i:
            stat = x
    conn.close()
    return stat


def get_temp_hum_for_table():
    """

        Функция для получения последних данных о воздухе для таблицы

    """
    conn = wrapper()
    cur = conn.cursor()
    st = get_temp_hum_num()
    cur.execute("CALL Get_temp_hum_for_table(?)", (st,))
    a = []
    b = []
    for t, h in cur:
        a.append(int(t))
        b.append(int(h))
    conn.close()
    return T_H_List(t_list=(a[::-1]), h_list=(b[::-1]))


def get_hum_for_table():
    """

        Функция для получения последних данных о почве для таблицы

    """
    conn = wrapper()
    cur = conn.cursor()
    st = get_hum_num()
    cur.execute("CALL Get_hum_for_table(?)", (st,))
    a = []
    for i in cur:
        for x in i:
            a.append(int(x))
    conn.close()
    return a[::-1]


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


def get_hum_soil(**kwargs):
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
        a.append(Temperature_Humidity(id=p_id, humidity=round(humidity, 2), tim=tim))
    conn.close()
    return a[::-1]


def get_temp_from_temp_hum():
    """

        Функция для получения всех значений температуры со всех датчиков воздуха для вычисления средней температуры

        :return: все значения температуры со всех датчиков воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    st = get_temp_hum_num() * 5
    cur.execute("CALL Get_temp_from_temp_hum(?)", (st,))
    a = []
    for a_id, i, t in cur:
        a.append(Temperature_Humidity(temperature=i, tim=t))
    conn.close()
    return a[::-1]


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
        a.append(Temperature_Humidity(id=p_id, temperature=round(temp, 2), humidity=round(hum, 2), tim=tim))
    conn.close()
    return a[::-1]


def get_hum_from_temp_hum():
    """

         Функция для получения всех значений влажности со всех датчиков воздуха для вычисления средней влажности

        :return: все значения влажности со всех датчиков воздуха

    """
    conn = wrapper()
    cur = conn.cursor()
    stat = get_temp_hum_num() * 5

    cur.execute("CALL Get_hum_from_temp_hum(?)", (stat,))
    a = []
    for a_id, i, t in cur:
        a.append(Temperature_Humidity(humidity=i, tim=t))
    conn.close()
    return a[::-1]


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
    for temp, hum in cur:
        a = Warnings(temperature=temp, humidity_air=hum)
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


def get_soil_warnings(**kwargs):
    """

    """
    conn = wrapper()
    cur = conn.cursor()
    cur.execute("CALL Get_soil_warnings(?)", (kwargs['id'],))
    a = ''
    for i, h in cur:
        a = Soil_Warnings(id=i, hb=h)
    conn.close()
    return a

