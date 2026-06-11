from datetime import date
from pydantic import BaseModel, ConfigDict


class ExpenseCreate(BaseModel):
    title: str
    amount: float
    category: str
    expense_date: date


class ExpenseResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    amount: float
    category: str
    expense_date: date