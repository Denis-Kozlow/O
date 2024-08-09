# from fastapi.testclient import TestClient
# from pytest import mark
from app.appl.main import app
# import app.appl.db

# client = TestClient(app)


# @mark.parametrize(
#     "dt, periods, amount, rate, expected_status, expected_json",
#     [
#         (
#             "31.01.2021",
#             3,
#             10000,
#             6,
#             200,
#             {
#                 '28.02.2021': 10050.0,
#                 '31.03.2021': 10100.25,
#                 '30.04.2021': 10150.75
#             },
#         ),
#     ],
# )
# def test_app(dt, periods, amount, rate, expected_status, expected_json):
#     assert 1 == 1
