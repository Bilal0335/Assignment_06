
"""
! 5. Static Variables and Static Methods

Assignment:
Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.
"""

# ! Solution:

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

result = MathUtils.add(20, 25)

print("=" * 40)
print("       🧮  MathUtils - Addition  🧮       ")
print("=" * 40)
print(f"The sum of 10 and 5 is: {result}")
print("=" * 40)
