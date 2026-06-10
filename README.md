# Expense Tracker API

A Dockerized REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** for managing expenses. The project also includes **Pytest** test cases and an **AWS Lambda function that interacts with Amazon S3**.

---

## Tech Stack

- FastAPI
- Pydantic v2
- PostgreSQL
- SQLAlchemy
- Docker & Docker Compose
- Pytest
- AWS Lambda
- Amazon S3

---

## Features

- Create a new expense
- View all expenses
- Delete an expense
- PostgreSQL database integration using SQLAlchemy
- Dockerized application
- Automated API testing with Pytest
- AWS Lambda function that reads data from an S3 bucket

---

## API Endpoints

| Method | Endpoint | Description |
|----------|------------|--------------------------|
| GET | `/` | Health check |
| POST | `/expenses` | Create a new expense |
| GET | `/expenses` | Retrieve all expenses |
| DELETE | `/expenses/{expense_id}` | Delete an expense |

---

## Project Structure

```
expense-tracker-api/
│
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── tests/
│   └── test_main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── queries.sql
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rohit111888/expense-tracker-api.git
cd expense-tracker-api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running with Docker

Build and start the application:

```bash
docker compose up --build
```

The API will be available at:

```
http://localhost:8000
```

Swagger documentation:

```
http://localhost:8000/docs
```

---

## Running Tests

```bash
pytest -v
```

Example output:

```
==========================
3 passed
==========================
```

---

## Database

The project uses PostgreSQL connected through SQLAlchemy.

Connection is configured using an environment variable:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/expense_db
```

---

## AWS Lambda + S3

An AWS Lambda function is included to demonstrate interaction with Amazon S3.

Functionality:

- Connects to an S3 bucket
- Reads a text file
- Returns its contents as a JSON response

Example response:

```json
{
    "statusCode": 200,
    "body": "{\"message\":\"Hi\"}"
}
```

---

## SQL

Sample SQL queries are provided in:

```
queries.sql
```

---

## Author

**Rohit Konatam**

GitHub: https://github.com/Rohit111888
