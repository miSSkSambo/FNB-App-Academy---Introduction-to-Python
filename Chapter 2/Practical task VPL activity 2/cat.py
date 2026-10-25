
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"{self.color} cat named {self.name} says meow!")

    def jump(self, height):
        print(f"The {self.color} cat jumps {height} meters high")


def demo():
    cat1 = Cat("Tom", "black")
    cat2 = Cat("Garfield", "orange")
    cat3 = Cat("JOHN", "purple")

    cat1.meow()
    cat2.meow()

    cat1.name = "Tiffany"
    cat2.color = "white"

    cat1.meow()
    cat2.meow()

    cat1.jump(2)
    cat2.jump(1.5)
    cat3.jump(3)


if __name__ == "__main__":
    demo()
