import datetime
import dateutil.parser
import time
import logging
import pytz
from typing import Literal, Union
from dateutil.relativedelta import relativedelta


    

def parseLocalizedDatetimes(time: Union[time.time, datetime.date, datetime.datetime, str, int, float], raiseError: bool = True) -> datetime.datetime:
    try:
        tz = pytz.timezone('CET')
        relevantTime = time
        if type(time) == datetime.date:
            relevantTime = datetime.datetime(year=time.year, month=time.month, day=time.day)
            logging.warning(f"date found")
            
        elif not isinstance(time, datetime.datetime):
            try:
                if isinstance(time, int) or isinstance(time, float) or str(time).strip('-').isnumeric():
                    time = float(time) / 1000
                return datetime.datetime.fromtimestamp(float(time), tz=tz)
            except:
                try:
                    relevantTime = dateutil.parser.parse(time, fuzzy=True)
                except:
                    if raiseError:
                        raise ValueError(f'Invaild locale time format >> {time} <<')
                    else:
                        return time
        # else:
        #     logging.warning(f"datetime found")
        #     return time
        if relevantTime.year < 1901:

            relevantTime = datetime.datetime(year=1901, month=1, day=1)
        elif relevantTime.year > 2999:
            relevantTime = datetime.datetime(year=2999, month=12, day=31)

        if relevantTime.tzinfo is not None:
            return relevantTime
        else: 
            return tz.localize(relevantTime)
    except OverflowError as of:
        raise OverflowError(f"{of}, {time} in parser")
    
    
def localeDatetimeToStr(timestemp:Union[time.time, datetime.date, datetime.datetime, str]=datetime.datetime.now(), 
                        to:Literal["unix", "wooMeta", "weclapp", "utc", "mip", "utcDate", "docName", "ads", "emailDate", "dateHour"] = "unix", raiseError:bool=True) -> str:

    try:
        timestemp = parseLocalizedDatetimes(time=timestemp)
    except ValueError as e:
        if raiseError:
            raise e
        else:
            return ""
    try:
        if to == "unix":
            return int(timestemp.timestamp())
        elif to == "weclapp":
            return int(timestemp.timestamp())*1000
        
        # used for email generation
        elif to == 'wooMeta' or to == "emailDate":
            return str(timestemp.strftime("%d.%m.%Y"))
        
        elif to == 'dateHour':    # woo = old
            return str(timestemp.strftime("%d.%m.%Y %H:%M"))
        
        elif to == 'utc' or to ==  "woo":    # woo = old
            return str(timestemp.strftime("%Y-%m-%dT%H:%M:%S"))
        elif to == 'utcDate':
            return str(timestemp.strftime("%Y-%m-%d"))
        elif to == 'mip':
            return str(timestemp.strftime("%Y-%m-%d"))
        elif to == "docName":
            return str(timestemp.strftime("%b-%Y"))
        elif to == "month":
            return str(timestemp.strftime("%Y-%b"))
        elif to == "ads":
            # 2022-12-04 11:11:11-01:00
            timezone = datetime.datetime.now(datetime.timezone.utc).astimezone()
            awareTime = datetime.datetime(timestemp.year, timestemp.month, timestemp.day, timestemp.hour, timestemp.minute, timestemp.second, tzinfo=timezone.tzinfo)
            # logging.info(f"{awareTime=}, {timestemp=}")
            return str(awareTime.isoformat().replace('T', ' '))
            # timezone = int(datetime.datetime.now(datetime.timezone.utc).astimezone().utcoffset().seconds / 3600)
            # part1 = str(timestemp.strftime("%Y-%m-%d %H:%M:%S"))
            # return f"{part1}+01:00"
        else: 
            return timestemp
    except OverflowError as of:
        raise OverflowError(f"{of}, {timestemp} while transforming to string")
    
    
    
def add(startTime: Union[time.time, datetime.date, datetime.datetime, str, int, float], 
                       years=0, months=0, days=0, leapdays=0, weeks=0,
                       hours=0, minutes=0, seconds=0, microseconds=0,
                       year=None, month=None, day=None, weekday=None,
                       yearday=None, nlyearday=None, hour=None, minute=None,
                       second=None, microsecond=None) -> datetime.datetime:
    """Parses a localized datetimeObject from a string or timestamp and adds the given time to it (timezone shifts aware)

    Returns:
        datetime.datetime: Localized and timezone normalized datetime object
    """
    try:
        startTime = parseLocalizedDatetimes(time=startTime)
    except ValueError:
        raise ValueError(f'---util.convertDateTimeTo()--- -> >>{startTime}<< not a datetimeobject')

        
    newDate = startTime + relativedelta(years=years, months=months, days=days, leapdays=leapdays, weeks=weeks,
                 hours=hours, minutes=minutes, seconds=seconds, microseconds=microseconds,
                 year=year, month=month, day=day, weekday=weekday,
                 yearday=yearday, nlyearday=nlyearday,
                 hour=hour, minute=minute, second=second, microsecond=microsecond)
    return startTime.tzinfo.normalize(newDate)
    