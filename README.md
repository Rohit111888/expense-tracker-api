# Expense Tracker API

A Dockerized REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy** for managing expenses. The project also includes **Pytest** test cases and an **AWS Lambda function that interacts with Amazon S3**.

---

## Tech Stack

* FastAPI
* Pydantic v2
* PostgreSQL
* SQLAlchemy
* Docker & Docker Compose
* Pytest
* AWS Lambda
* Amazon S3

---

## Features

* Create a new expense
* Retrieve all expenses
* Delete an expense
* Health check endpoint
* PostgreSQL integration using SQLAlchemy ORM
* Dockerized deployment
* Automated API testing with Pytest
* AWS Lambda function that reads data from Amazon S3

---

## API Endpoints

| Method | Endpoint                 | Description           |
| ------ | ------------------------ | --------------------- |
| GET    | `/`                      | Health check          |
| POST   | `/expenses`              | Create a new expense  |
| GET    | `/expenses`              | Retrieve all expenses |
| DELETE | `/expenses/{expense_id}` | Delete an expense     |

---

## Project Structure

```text
expense-tracker-api/
│
├── app/
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── aws_lambda.py
│
├── lambda_s3/
│   └── lambda_function.py
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

```bash
git clone https://github.com/Rohit111888/expense-tracker-api.git
cd expense-tracker-api
pip install -r requirements.txt
```

---

## Running with Docker

```bash
docker compose up --build
```

API:

```
http://localhost:8000
```

Swagger UI:

```
http://localhost:8000/docs
```

---

## Running Tests

```bash
pytest -v
```

Example:

```
==========================
3 passed
==========================
```

---

## Database

The application uses PostgreSQL connected through SQLAlchemy.

Example:

```
DATABASE_URL=postgresql://postgres:password@localhost:5432/expense_db
```

---

## AWS Lambda + Amazon S3

This project includes an AWS Lambda function that demonstrates interaction with Amazon S3.

Functionality:

* Connects to an S3 bucket
* Reads a text file
* Returns the file contents as a JSON response

Example:

```json
{
    "statusCode": 200,
    "body": "{\"message\":\"Hi\"}"
}
```

---

## SQL

Sample SQL queries are available in:

```
queries.sql
```

---

## Screenshots

* FastAPI Swagger UI
* Dockerized application
* Pytest execution
* AWS Lambda deployment
* Lambda execution
* Amazon S3 bucket

---

## Author

**Rohit Konatam**

GitHub: https://github.com/Rohit111888
