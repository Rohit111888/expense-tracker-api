from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models, schemas, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")


def get_db():
    """
    Create and provide a database session for each API request.

    Yields:
        A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home() -> dict:
    """
    Return a health check message for the API.

    Returns:
        A dictionary confirming that the API is running.
    """
    return {"message": "Expense Tracker API is running!"}


@app.post("/expenses", response_model=schemas.ExpenseResponse)
def add_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    """
    Create a new expense using request body data.

    Args:
        expense: Validated expense data from the request body.
        db: Active SQLAlchemy database session.

    Returns:
        The newly created expense record.
    """
    return crud.create_expense(db, expense)


@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
def read_expenses(db: Session = Depends(get_db)):
    """
    Retrieve all expenses from the database.

    Args:
        db: Active SQLAlchemy database session.

    Returns:
        A list of expense records.
    """
    return crud.get_expenses(db)


@app.delete("/expenses/{expense_id}")
def remove_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    """
    Delete an expense by its ID.

    Args:
        expense_id: ID of the expense to delete.
        db: Active SQLAlchemy database session.

    Returns:
        A success message if the expense is deleted.

    Raises:
        HTTPException: If the expense is not found.
    """
    deleted = crud.delete_expense(db, expense_id)

    if deleted is None:
        raise HTTPException(status_code=404, detail="Expense not found")

    return {"message": "Expense deleted successfully"}