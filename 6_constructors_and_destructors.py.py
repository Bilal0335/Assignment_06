"""
! 6. Constructors and Destructors

Assignment:
Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).

"""
# ! Solution:

class Logger:
    def __init__(self):
        print("Logger created!")

    def __del__(self):
        print("Logger destroyed!")


logger = Logger()
del logger
