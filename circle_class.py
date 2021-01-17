class Circle():
    # Class object Attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius * radius * Circle.pi

    # METHOD
    def get_circumference(self):
        return self.radius * Circle.pi * 2


# Main piece of the program
my_circle = Circle(30)
print(my_circle.pi)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)
