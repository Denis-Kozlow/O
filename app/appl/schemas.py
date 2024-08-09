import pandas as pd
from pydantic import BaseModel, field_validator
from fastapi import HTTPException
from datetime import datetime

FORM = "%d.%m.%Y"


class SDepAdd(BaseModel):
    date: str | datetime
    periods: int
    amount: int
    rate: float

    @field_validator('date')
    def validate_date(cls, value):
        try:
            valid_date = pd.to_datetime(value, format=FORM)
        except ValueError:
            raise HTTPException(status_code=400, detail={
                                "error date": "Не верный формат даты. Ожидаемый: dd.mm.YYYY"})
        return valid_date

    @field_validator('periods')
    def validate_periods(cls, value):
        if value < 1 or value > 60:
            raise HTTPException(status_code=400, detail={
                                "error periods": "Не верное число. Ожидается: от 1 до 60"})
        return value

    @field_validator('amount')
    def validate_amount(cls, value):
        if value < 10_000 or value > 3_000_000:
            raise HTTPException(status_code=400, detail={
                                "error amount": "Не верное число. Ожидается: от 10_000 до 3_000_000"})
        return value

    @field_validator('rate')
    def validate_rate(cls, value):
        if value < 1 or value > 8:
            raise HTTPException(status_code=400, detail={
                                "error rate": "Не верное число. Ожидается: от 1 до 8"})
        return value
