from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy import text

from database import engine

app = FastAPI()


# Model for creating a student
class Student(BaseModel):
    name: str
    roll_no: str
    maths: Optional[int] = None
    english: Optional[int] = None
    science: Optional[int] = None
    computer: Optional[int] = None


# Model for updating a student
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    roll_no: Optional[str] = None
    maths: Optional[int] = None
    english: Optional[int] = None
    science: Optional[int] = None
    computer: Optional[int] = None


@app.get("/")
def index():
    return {"Message": "Student Management API is running"}


@app.get("/get-student/{student_id}")
def get_student(student_id: int):

    query = text("""
        SELECT *
        FROM Students
        WHERE id = :student_id
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"student_id": student_id}
        )

        student = result.mappings().first()

    if student is None:
        return {"Error": "Student doesn't exist"}

    return dict(student)


@app.get("/get-by-name")
def get_student_by_name(name: str):

    query = text("""
        SELECT *
        FROM Students
        WHERE name = :name
    """)

    with engine.connect() as connection:
        result = connection.execute(
            query,
            {"name": name}
        )

        students = result.mappings().all()

    if not students:
        return {"Data": "Not found"}

    return [dict(student) for student in students]


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):

    check_query = text("""
        SELECT id
        FROM Students
        WHERE id = :student_id
    """)

    insert_query = text("""
        INSERT INTO Students
        (id, name, roll_no, maths, english, science, computer)
        VALUES
        (:id, :name, :roll_no, :maths, :english, :science, :computer)
    """)

    with engine.begin() as connection:

        existing_student = connection.execute(
            check_query,
            {"student_id": student_id}
        ).first()

        if existing_student is not None:
            return {"Error": "Student already exists"}

        student_data = student.model_dump()
        student_data["id"] = student_id

        connection.execute(
            insert_query,
            student_data
        )

    return {
        "Message": "Student created successfully",
        "id": student_id,
        **student.model_dump()
    }


@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):

    student_data = student.model_dump(exclude_unset=True)

    if not student_data:
        return {"Error": "No data provided for update"}

    allowed_columns = {
        "name", "roll_no", "maths",
        "english", "science", "computer"
    }

    update_fields = {
        key: value
        for key, value in student_data.items()
        if key in allowed_columns
    }

    set_clause = ", ".join(
        f"{column} = :{column}"
        for column in update_fields
    )

    query = text(f"""
        UPDATE Students
        SET {set_clause}
        WHERE id = :student_id
    """)

    with engine.begin() as connection:

        result = connection.execute(
            query,
            {
                **update_fields,
                "student_id": student_id
            }
        )

        if result.rowcount == 0:
            return {"Error": "Student doesn't exist"}

    return get_student(student_id)


@app.patch("/patch-student/{student_id}")
def patch_student(student_id: int, student: UpdateStudent):

    student_data = student.model_dump(exclude_unset=True)

    if not student_data:
        return {"Error": "No data provided for update"}

    allowed_columns = {
        "name", "roll_no", "maths",
        "english", "science", "computer"
    }

    update_fields = {
        key: value
        for key, value in student_data.items()
        if key in allowed_columns
    }

    set_clause = ", ".join(
        f"{column} = :{column}"
        for column in update_fields
    )

    query = text(f"""
        UPDATE Students
        SET {set_clause}
        WHERE id = :student_id
    """)

    with engine.begin() as connection:

        result = connection.execute(
            query,
            {
                **update_fields,
                "student_id": student_id
            }
        )

        if result.rowcount == 0:
            return {"Error": "Student doesn't exist"}

    return get_student(student_id)


# DELETE: Delete a student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):

    select_query = text("""
        SELECT *
        FROM Students
        WHERE id = :student_id
    """)

    delete_query = text("""
        DELETE FROM Students
        WHERE id = :student_id
    """)

    with engine.begin() as connection:

        result = connection.execute(
            select_query,
            {"student_id": student_id}
        )

        student = result.mappings().first()

        if student is None:
            return {"Error": "Student doesn't exist"}

        deleted_student = dict(student)

        connection.execute(
            delete_query,
            {"student_id": student_id}
        )

    return {
        "Message": "Student deleted successfully",
        "Student": deleted_student
    }