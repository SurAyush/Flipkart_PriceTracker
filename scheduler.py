from tracker import get_price


import schedule
import time


schedule.every(2).minutes.do(get_price)

while True:
    schedule.run_pending()
    time.sleep(1)