class Animal():

    def __init__(self):
        print("ANIMAL Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")

class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")

    def who_am_i(self):
        print("I am a dog")

    def eat(self):
        print("I am a dog and eating")

    def bark(self):
        print("WOOF!!")





my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()
my_dog.bark()
my_dog.eat()

my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()


