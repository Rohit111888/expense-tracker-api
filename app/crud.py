from sqlalchemy.orm import Session
from app import models, schemas


def create_expense(db: Session, expense: schemas.ExpenseCreate):
    new_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        expense_date=expense.expense_date
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


def get_expenses(db: Session):
    return db.query(models.Expense).all()


def delete_expense(db: Session, expense_id: int):
    expense = (
        db.query(models.Expense)
        .filter(models.Expense.id == expense_id)
        .first()
    )

    if expense:
        db.delete(expense)
        db.commit()

    return expense