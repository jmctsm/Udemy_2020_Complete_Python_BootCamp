class Dog():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow!"


niko = Dog("niko")
felix = Cat("felix")

print(niko.speak())
print(felix.speak())

def pet_speak(pet):
    print(pet.speak())

for pet in [niko, felix]:
    print(type(pet))
    print(type(pet.speak()))
    print(pet.speak())

pet_speak(niko)


class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("SubClass must implement this abtstact method")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof!!"

class Cat(Animal):
    def speak(self):
        return self.name + " says meow!!"

#my_animal = Animal("Fred")
#my_animal.speak()

fido = Dog("Fido")
isis = Cat("Isis")

print(fido.speak())
print(isis.speak())
