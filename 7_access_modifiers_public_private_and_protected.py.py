
"""
! 7. Access Modifiers: Public, Private, and Protected

Assignment:
Create a class Employee with:

a public variable name,

a protected variable _salary, and

a private variable __ssn.

Try accessing all three variables from an object of the class and document what happens.
"""

# ! Solution:

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        # Public variable
        self._salary = salary   # Protected variable
        self.__ssn = ssn        # Private variable


# Creating an object of Employee
emp = Employee("Bilal Hussain", 50000, "123-45-6789")

# Accessing the public variable
print("Name:", emp.name)  

# Accessing the protected variable
print("Salary:", emp._salary)  

# Accessing the private variable
try:
    print("SSN:", emp.__ssn)  

except AttributeError as e:
    print("Error accessing SSN:", e)

# Correct way to access private variable (name mangling)
print("SSN (accessed correctly):", emp._Employee__ssn) 
