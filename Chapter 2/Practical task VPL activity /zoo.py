
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def makeSound(self):
        print(f"My name is {self.name} and I am {self.age} years old")


class Lion(Animal):
    def __init__(self, name, age, furrcolor):
        super().__init__(name, age)
        self.furrcolor = furrcolor

    def makeSound(self):
        super().makeSound()
        print("ROARRRR")


class Snake(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def makeSound(self):
        super().makeSound()
        print("HISSSSS")


class Elephant(Animal):
    def __init__(self, name, age, trunkLength):
        super().__init__(name, age)
        self.trunkLength = trunkLength

    def makeSound(self):
        super().makeSound()
        print("GORRRRRRR")


class ZOO:
    def __init__(self):
        self.animals = []

    def addAnimal(self, animal):
        self.animals.append(animal)

    def removeAnimal(self, animal):
        self.animals.remove(animal)


def demo():
    Z1 = ZOO()

    lion = Lion("Simba", 5, "golden")
    snake = Snake("Sly", 2)

    Z1.addAnimal(lion)
    Z1.addAnimal(snake)

    # Test 1: Lion and snake
    for animal in Z1.animals:
        animal.makeSound()

    # TODO 5: Create and add an elephant
    elephant = Elephant("Dumbo", 10, 2.5)
    Z1.addAnimal(elephant)

    # Test 2: Lion, snake, and elephant
    for animal in Z1.animals:
        animal.makeSound()

    # Test 3: Remove the lion
    Z1.removeAnimal(lion)
    for animal in Z1.animals:
        animal.makeSound()


if __name__ == "__main__":
    demo()
