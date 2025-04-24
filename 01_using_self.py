
"""
! 1. Using self

Assignment:

Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.
"""

# * Solution:
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("=" * 25)
        print("   Student Details")
        print("=" * 25)
        print(f"Name  : {self.name.title()}")
        print(f"Marks : {self.marks}")
        print("=" * 25)

        
student_01 = Student("m. bilal hussain",85)
student_01.display()
        