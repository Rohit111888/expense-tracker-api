import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Loading environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Creating PostgreSQL engine
engine = create_engine(DATABASE_URL)

# Creating session
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class for models
Base = declarative_base()