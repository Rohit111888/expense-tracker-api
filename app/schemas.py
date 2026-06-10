from pydantic import BaseModel, ConfigDict
from datetime import date


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    expense_date: date


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: str
    expense_date: date

    model_config = ConfigDict(from_attributes=True)