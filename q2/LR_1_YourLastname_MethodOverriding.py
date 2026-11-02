class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

    def eat(self):
        pass


class Lion(Animal):
    def make_sound(self):
        print("The lion roars loudly; ", end="")

    def eat(self):
        print("the lion eats fresh meat.")


class Elephant(Animal):
    def make_sound(self):
        print("The elephant trumpets; ", end="")

    def eat(self):
        print("the elephant eats grass and fruits.")


class Monkey(Animal):
    def make_sound(self):
        print("The monkey chatters; ", end="")

    def eat(self):
        print("the monkey eats bananas.")


lion = Lion("lion")
elephant = Elephant("elephant")
monkey = Monkey("monkey")

animals = [lion, elephant, monkey]

for animal in animals:
    animal.make_sound()
    animal.eat()