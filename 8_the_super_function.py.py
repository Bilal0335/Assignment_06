
"""
! 8. The super() Function

Assignment:
Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.
"""

# ! Solution:

# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject

# Create an object of Teacher
teacher = Teacher("Sir Aneeq ", "Python Programming")


print("Name:", teacher.name)
print("Subject:", teacher.subject)
