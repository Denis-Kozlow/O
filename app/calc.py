from datetime import datetime
from dateutil.relativedelta import relativedelta


FORMAT = "%d.%m.%Y"


def calc_date(date, period):
    return [(date + relativedelta(months=i+1)).strftime(FORMAT) for i in range(period)]


def calc_summ(amount, periods, rate):
    return [round(amount * pow(1 + rate / 100 / 12, i + 1), 2) for i in range(periods)]


def ret_dep(depos):
    date = calc_date(depos.date, depos.periods)
    summ = calc_summ(depos.amount, depos.periods, depos.rate)
    res = {i[0]: i[1] for i in zip(date, summ)}

    return res
