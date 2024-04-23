#it will execute the tracker.py file after every 30 minutes to monitor and note down the price of the products

from tracker import get_price_caller

import schedule
import time

#scheduling event after every 30 minutes
#get_price function will be called after every 30 minutes
schedule.every(15).seconds.do(get_price_caller)

#waiting till the function is executed
while True:
    schedule.run_pending()
    time.sleep(1)