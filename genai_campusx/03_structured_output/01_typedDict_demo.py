
from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person: Person = {
    'name': 'David',
    'age': 31
}

print("Person Obj:", new_person)