import db
from schemas import Warnings, Temperature_Humidity


# ----------------------------------------------------Create py-tests--------------------------------------------------#


def test_create_fork():
    assert db.create_fork() == 'Ok'


def test_create_hum():
    q = ''
    for i in range(1, 7):
        q = db.create_hum(temperature_humidity=Temperature_Humidity(id=i, humidity=60.0, tim='10:00'))
    assert q == 'Ok'


def test_create_temp_hum():
    q = ''
    for i in range(1, 5):
        q = db.create_temp_hum(temperature_humidity=Temperature_Humidity(id=i, humidity=60.0, temperature=30.0,
                                                                         tim='10:00'))
    assert q == 'Ok'


def test_create_total_hum():
    assert db.create_total_hum() == 'Ok'


def test_create_watering():
    q = ''
    for i in range(1, 7):
        q = db.create_watering(id=i)
    assert q == 'Ok'


def test_create_warnings():
    assert db.create_warnings() == 'Ok'


# ----------------------------------------------------Get py-tests-----------------------------------------------------#


def test_get_fork():
    assert db.get_fork() == 0


def test_get_hum():
    assert db.get_hum(id=1) == [Temperature_Humidity(id=1, humidity=60.0, tim='10:00')]


def test_get_temp_from_temp_hum():
    assert db.get_temp_from_temp_hum() == [30, 30, 30, 30]


def test_get_hum_temp():
    assert db.get_hum_temp(id=1) == [Temperature_Humidity(id=1, humidity=60.0, temperature=30.0, tim='10:00')]


def test_get_hum_from_temp_hum():
    assert db.get_hum_from_temp_hum() == [60, 60, 60, 60]


def test_get_total_hum():
    assert db.get_total_hum() == 0


def test_get_warnings():
    assert db.get_warnings() == Warnings(temperature=20.0, humidity_air=70.0, humidity_soil=50.0)


def test_get_watering():
    assert db.get_watering(id=1) == 0


# ----------------------------------------------------Put py-tests-----------------------------------------------------#


def test_change_fork():
    assert db.change_fork() == 'Ok'


def test_change_total_hum():
    assert db.change_total_hum() == 'Ok'


def test_change_watering():
    q = ''
    for i in range(1, 7):
        q = db.change_watering(id=i)
    assert q == 'Ok'


def test_change_warnings_temp():
    assert db.change_warnings_temp(temperature=25.0) == 'Ok'


def test_change_warnings_h():
    assert db.change_warnings_h(humidity_air=60.0) == 'Ok'


def test_change_warnings_hb():
    assert db.change_warnings_hb(humidity_soil=30.0) == 'Ok'
