import requests
from constants import arduino_link


def change_watering_system(state: int):
    requests.get(f"{arduino_link}/change_pump_state/{state}")


def change_fork_state(state: int):
    requests.get(f"{arduino_link}/change_fork_state/{state}")


def change_total_hum_state(state: int):
    requests.get(f"{arduino_link}/change_total_hum/{state}")