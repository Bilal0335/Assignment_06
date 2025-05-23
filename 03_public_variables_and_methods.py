
"""
! 3. Public Variables and Methods

Assignment:
Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


"""
# ! Solution

class Car:
    def __init__(self, brand):
        self.brand = brand  

    def start(self):  
        print(f"The {self.brand} car is starting...")


my_car = Car("Toyota")

print("Brand:", my_car.brand)
my_car.start()
