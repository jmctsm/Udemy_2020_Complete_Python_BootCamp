class Dog():

    # Class object atrribute
    # same for any instance of a class
    species = "mammal"

    def __init__(self, breed, name, spots):
        # Attributes
        # we take in the argument
        # assign it use the self.attribute_name
        self.breed = breed
        self.name = name

        # Expect boolean True/False
        self.spots = spots

    # Operations/Actions --> Methods
    def bark(self, number):
        print("WOOF!!!!  My name is {} and the number is {}".format(self.name, number))


my_dog = Dog(breed="lab", name="Sammy", spots="NO SPOTS")

print(my_dog)
print(my_dog.name)
print(my_dog.breed)
print(my_dog.spots)
print(my_dog.species)
print(type(my_dog))
my_dog.bark(4)
