
from typing import Optional, List

from pydantic import BaseModel


class Temperature_Humidity(BaseModel):
    """
        Класс для всех датчиков
    """
    id: Optional[int]
    humidity: Optional[float]
    temperature: Optional[float]
    tim: Optional[str]


class Watering(BaseModel):
    """
        Класс для систем полива
    """
    id: Optional[int]
    state: Optional[int]


class Warnings(BaseModel):
    """

        Класс для порогов средних значений воздуха

    """
    temperature: Optional[int]
    humidity_air: Optional[int]


class List_Temperature_Humidity(BaseModel):
    temp_hums: List[Temperature_Humidity]


class Average_List(BaseModel):
    """
        Класс для средних значений
    """
    d_list: List[float]
    t_list: List[str]


class T_H_List(BaseModel):
    """
        Класс для последних 5 значаний с одного датчика
    """
    id: Optional[int]
    t_list: Optional[list]
    h_list: Optional[list]
    tim_list: Optional[list]


class Soil_Warnings(BaseModel):
    """

            Класс для порогов средних значений почвы

    """

    id: Optional[int]
    hb: Optional[float]
