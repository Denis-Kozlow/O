from app.appl.calc import ret_dep, calc_date, calc_summ
from pytest import mark, raises
from app.appl.schemas import SDepAdd
from datetime import datetime
from contextlib import nullcontext as does_not_raise


@mark.parametrize(
    "da, per, am, rat, res, expectation",
    [
        ("31.01.2021", 3, 10000, 6,
         {
             "28.02.2021": 10050,
             "31.03.2021": 10100.25,
             "30.04.2021": 10150.75
         },
            does_not_raise()),
        ("30.07.2025", 1, 10000, 2,
         {
             '30.08.2025': 10015.67},
         raises(AssertionError))
    ]
)
def test_sys(da, per, am, rat, res, expectation):
    with expectation:
        p = SDepAdd(date=da, periods=per,
                    amount=am, rate=rat)
        assert ret_dep(p) == res


@mark.parametrize(
    "amount, periods, rate, res",
    [
        (11_111, 21, 5.6,
         [11162.85, 11214.94, 11267.28,
          11319.86, 11372.69, 11425.76,
          11479.08, 11532.65, 11586.47,
          11640.54, 11694.86, 11749.44,
          11804.27, 11859.35, 11914.7,
          11970.3, 12026.16, 12082.28,
          12138.67, 12195.31, 12252.23])
    ]
)
def test_summ(amount, periods, rate, res):
    assert calc_summ(amount, periods, rate) == res


@mark.parametrize(
    "date, period, res",
    [
        (datetime(2020, 5, 29), 49,
         ['29.06.2020', '29.07.2020', '29.08.2020',
         '29.09.2020', '29.10.2020', '29.11.2020',
          '29.12.2020', '29.01.2021', '28.02.2021',
          '29.03.2021', '29.04.2021', '29.05.2021',
          '29.06.2021', '29.07.2021', '29.08.2021',
          '29.09.2021', '29.10.2021', '29.11.2021',
          '29.12.2021', '29.01.2022', '28.02.2022',
          '29.03.2022', '29.04.2022', '29.05.2022',
          '29.06.2022', '29.07.2022', '29.08.2022',
          '29.09.2022', '29.10.2022', '29.11.2022',
          '29.12.2022', '29.01.2023', '28.02.2023',
          '29.03.2023', '29.04.2023', '29.05.2023',
          '29.06.2023', '29.07.2023', '29.08.2023',
          '29.09.2023', '29.10.2023', '29.11.2023',
          '29.12.2023', '29.01.2024', '29.02.2024',
          '29.03.2024', '29.04.2024', '29.05.2024',
          '29.06.2024'])

    ]
)
def test_date(date, period, res):
    assert calc_date(date, period) == res
