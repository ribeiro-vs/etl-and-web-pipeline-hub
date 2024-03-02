from datetime import datetime
from googletrans import Translator
from datetime import timedelta
from datetime import datetime
import pandas as pd
from dateutil.relativedelta import relativedelta
import time
from verifiers import process_registrant

"""
    It is strictly for the purposes of:
        - Store time-related classes.
"""

class Timer:

    def __init__(self):
        self.start=None
        self.finish=None
        self.minutes=None
        self.seconds=None

    def start_count(self):
        self.start = (datetime.today()).strftime('%HH:%MM:%SS') 
        self.start_time = time.time()

    def finish_count(self):
        self.finish = (datetime.today()).strftime('%HH:%MM:%SS')
        end_time = time.time()
        time_elapsed = end_time - self.start_time
        self.minutes, self.seconds = divmod(time_elapsed, 60)
        
class Metabase_date_format():

    @property
    def d_minus_one(self):
        return(datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
    @property
    def today(self):
        return(datetime.today() - timedelta()).strftime('%Y-%m-%d') 
    @property
    def today_minus_63(self):
        return(datetime.today() - timedelta(days=63) ).strftime('%Y-%m-%d') 
    @property
    def yesterday(self):
        return(datetime.today() - timedelta(days=1) ).strftime('%Y-%m-%d')
    @property
    def current_month_first_day(self):
        return(datetime.today() - timedelta(days=1) ).strftime('%Y-%m-01')
    @property
    def current_month_last_day(self):
        return(pd.Period(datetime.today() - timedelta(days=1),freq='M').end_time.date().strftime('%Y-%m-%d'))
    @property
    def past_month_first_day(self):
        return(datetime.today() - relativedelta(months=1)).strftime('%Y-%m-01')
    @property
    def past_month_last_day(self):
        return(pd.Period(datetime.today() - relativedelta(months=1),freq='M').end_time.date().strftime('%Y-%m-%d'))
    @property
    def next_month_fifteenth_day(self):
        return(datetime.today() - relativedelta(months=-1)).strftime('%Y-%m-15')
    @property
    def next_fifteen_days(self):
        return(datetime.today() - timedelta(days=-15)).strftime('%Y-%m-%d')
    @property
    def past_thirty_first_day(self):
        return(datetime.today() - timedelta(days=31)).strftime('%Y-%m-%d')
    @property
    def current_year_first_day(self):
        return(datetime.today() - timedelta(days=1) ).strftime('%Y-01-01')
    @property
    def current_year_last_day(self):
        return(datetime.today() - timedelta(days=1) ).strftime('%Y-12-31')
    @property
    def six_months_ago_first_day(self):
        return(datetime.today() - relativedelta(months=6)).strftime('%Y-%m-01')
    @property
    def thirty_days_before(self):
        return(datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    @property
    def thirty_days_ahead(self):
        return(datetime.today() - timedelta(days=-30)).strftime('%Y-%m-%d')
    @property
    def two_months_ago_first_day(self):
        return(datetime.today() - relativedelta(months=2)).strftime('%Y-%m-%d')
    @property
    def past_ninety_five_days(self):
        return(datetime.today() - timedelta(days=95)).strftime('%Y-%m-%d')
    
class Alternative_date_variables():

    @property
    def today(self):
        return (datetime.today()).strftime('%m/%d/%Y')
    @property
    def today_dd_mm_yyyy_with_hyphen(self):
        return (datetime.today()).strftime('%d-%m-%Y')
    @property
    def past_month_first_day_dd_mm_yyyy_with_slash(self):
        return (datetime.today() - relativedelta(months=1)).strftime('01/%m/%Y')
    @property
    def current_month_last_day_dd_mm_yyyy_with_slash(self):
        return(pd.Period(datetime.today() - timedelta(days=1),freq='M').end_time.date().strftime('%d/%m/2023'))
    @property
    def alternative_extraction_day_03(self):
        return (datetime.today()).strftime('%m/02/%Y')
    @property
    def yesterday_slash_separated_mm_dd_yyyy(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m/%d/%Y')
    @property
    def yesterday_hyphen_separated_mm_dd_yyyy(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m-%d-%Y')
    @property
    def yest_str(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m%d%Y')
    @property
    def year_month(self):
        return (datetime.today() - timedelta(days=1)).strftime('%Y%m')
    @property
    def month_year(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m%Y')
    @property
    def month_hyphen_year(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m-%Y')
    @property
    def year_hyphen_month(self):
        return (datetime.today() - timedelta(days=1)).strftime('%Y-%m')
    @property
    def past_month_year_month(self):
        return (datetime.today() - relativedelta(months=1)).strftime('%Y%m')
    @property
    def month_dot_year(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m.%Y')
    @property
    def month_dot_year_two_digits_each(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m.%y')
    @property
    def month_year_two_digits_each(self):
        return (datetime.today() - timedelta(days=1)).strftime('%m%y')
    @property
    def year(self):
        return (datetime.today()).strftime('%Y')
    @property
    def year_two_digits(self):
        return (datetime.today()).strftime('%y')
    @property
    def month_name_capitalized(self):
        translated_text = Translator().translate((datetime.today() - timedelta(days=1)).strftime("%B"), src='en', dest='pt')
        if translated_text is not None:
            month_name_capitalized = translated_text.text.capitalize()
        else:
            month_name_capitalized = None
            process_registrant.register_error('ERROR GOOGLETRANS')
        if month_name_capitalized == 'Marchar': 
            month_name_capitalized = 'Março' 
        return month_name_capitalized
    
class Time_formats():
    
    @property
    def hour(self):
        return (datetime.today() - timedelta(hours=1)).strftime('%H')