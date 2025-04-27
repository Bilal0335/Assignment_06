

"""
! 19. callable() and __call__()
Assignment:
Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.

"""
# ! Solution

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor

# Create object
mult = Multiplier(3)

# Check callable
print(callable(mult))  # True

# Call like function
print(mult(5))  # 15
