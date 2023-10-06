from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)

DAYS_LIST = timedelta(days=100)
YEAR_LIST = timedelta(days=365)

def gen_special_pybites_dates():
    days_end = PYBITES_BORN + YEAR_LIST * 100
    start_date = PYBITES_BORN
    sto_days = timedelta(days=+100)


    while True:
        start_date += DAYS_LIST
        if start_date < days_end:
            yield start_date
        
    else:
        start_date += sto_days
        yield start_date   