import time

import schedule

import api


def create():
    api.create_hum()
    api.create_temp_hum()


schedule.every().hour.at(":00").do(create)
schedule.every().hour.at(":05").do(create)
schedule.every().hour.at(":10").do(create)
schedule.every().hour.at(":15").do(create)
schedule.every().hour.at(":20").do(create)
schedule.every().hour.at(":25").do(create)
schedule.every().hour.at(":30").do(create)
schedule.every().hour.at(":35").do(create)
schedule.every().hour.at(":40").do(create)
schedule.every().hour.at(":45").do(create)
schedule.every().hour.at(":50").do(create)
schedule.every().hour.at(":55").do(create)


while True:
    schedule.run_pending()
    time.sleep(1)