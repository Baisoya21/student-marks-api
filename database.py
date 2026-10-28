from sqlalchemy import create_engine

DATABASE_URI = "sqlite:///./students.db"

A = DATABASE_URI

engine = create_engine(A)

try:
    with engine.connect() as connection:
     print("Database connection successful!")

except Exception as e:
    print("Database connection failed!")
    print("Error:", e)
