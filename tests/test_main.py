from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Expense Tracker API is running!"
    }


def test_get_expenses():
    response = client.get("/expenses")
    assert response.status_code == 200


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Coffee",
            "amount": 5.50,
            "category": "Food",
            "expense_date": "2026-06-10"
        }
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Coffee"