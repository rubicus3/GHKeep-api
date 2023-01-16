
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
        Класс для порогов средних значений
    """
    temperature: Optional[int]
    humidity_air: Optional[int]
    humidity_soil: Optional[int]


class List_Temperature_Humidity(BaseModel):
    temp_hums: List[Temperature_Humidity]



