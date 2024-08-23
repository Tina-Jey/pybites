from pytz import timezone, utc
from datetime import datetime


AUSTRALIA = timezone('Australia/Sydney')
SPAIN = timezone('Europe/Madrid')

def what_time_lives_pybites(naive_utc_dt):
    """Receives a naive UTC datetime object and returns a two element
       tuple of Australian and Spanish (timezone aware) datetimes"""
    
    aware_dt_utc = naive_utc_dt.replace(tzinfo=utc)

    aust_time = aware_dt_utc.astimezone(AUSTRALIA)
    sp_time = aware_dt_utc.astimezone(SPAIN)

    return aust_time, sp_time