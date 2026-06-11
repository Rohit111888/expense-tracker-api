from sqlalchemy.orm import Session
from app import models, schemas


def create_expense(db: Session, expense: schemas.ExpenseCreate) -> models.Expense:
    """
    Insert a new expense record into the database.

    Args:
        db: Active SQLAlchemy database session.
        expense: Validated expense data from the request body.

    Returns:
        The newly created Expense ORM object with its assigned ID.
    """
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


def get_expenses(db: Session) -> list[models.Expense]:
    """
    Retrieve all expense records from the database.

    Args:
        db: Active SQLAlchemy database session.

    Returns:
        A list of Expense ORM objects.
    """
    return db.query(models.Expense).all()


def delete_expense(db: Session, expense_id: int) -> models.Expense | None:
    """
    Delete an expense record by its ID.

    Args:
        db: Active SQLAlchemy database session.
        expense_id: ID of the expense to delete.

    Returns:
        The deleted Expense ORM object if found, otherwise None.
    """
    expense = db.query(models.Expense).filter(models.Expense.id == expense_id).first()

    if expense:
        db.delete(expense)
        db.commit()

    return expense