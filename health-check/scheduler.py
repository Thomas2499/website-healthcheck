from .consts import HEALTH_CHECK_INTERVAL_SECONDS
from .health_check import check_website_health
import schedule
import time


def create_scheduled_check():
    check_website_health()
    schedule.every(HEALTH_CHECK_INTERVAL_SECONDS).seconds.do(check_website_health)
    while True:
        schedule.run_pending()
        time.sleep(1)
