
from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):
    name: str = 'Peter'
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=11, default=5, description='A decimal value representing the cgpa of the student')

new_student = {
    'age': 32,
    'email': 'abc@example.com',
}

student = Student(**new_student)

student_dict = dict(student)

student_json = student.model_dump_json()

# print(f"student object: {dict(student)}")

print(f"Student Age: {student_dict['age']}")
print(f"Student JSON: {student_json}")