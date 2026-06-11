from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app import models, schemas, crud
from app.aws_lambda import export_expenses_to_s3

# Creating tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API"
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"message": "Expense Tracker API is running!"}


@app.post("/expenses", response_model=schemas.ExpenseResponse)
def add_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    return crud.create_expense(db, expense)


@app.get("/expenses", response_model=list[schemas.ExpenseResponse])
def read_expenses(db: Session = Depends(get_db)):
    return crud.get_expenses(db)


@app.delete("/expenses/{expense_id}")
def remove_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_expense(db, expense_id)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return {"message": "Expense deleted successfully"}


@app.get("/expenses/export")
def export_expenses(db: Session = Depends(get_db)):
    expenses = crud.get_expenses(db)

    expense_list = []

    for expense in expenses:
        expense_list.append({
            "id": expense.id,
            "title": expense.title,
            "amount": expense.amount,
            "category": expense.category,
            "expense_date": str(expense.expense_date)
        })

    lambda_response = export_expenses_to_s3(expense_list)

    return {
        "message": "Expenses exported successfully",
        "lambda_response": lambda_response
    }