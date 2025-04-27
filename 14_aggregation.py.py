

"""
! 14. Aggregation
Assignment:
Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

"""
# ! Solution

class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)


emp1 = Employee("Alice")
emp2 = Employee("Bob")

dept = Department("HR")
dept.add_employee(emp1)
dept.add_employee(emp2)

print(f"Department: {dept.dept_name}")
for emp in dept.employees:
    print("Employee:", emp.name)
