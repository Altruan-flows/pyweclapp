from .localizedTime import *
import datetime


def timeDifferenceMonths(t1:datetime.datetime, t2:datetime.datetime):
    t1 = parse(t1)
    t2 = parse(t2)

    if t1 > t2:
        t1, t2 = t2, t1
    deltaYear = t2.year - t1.year
    deltaMonth = t2.month - t1.month
    return deltaYear * 12 + deltaMonth
    