# Define the Dog class
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name:", self.name)
        print("Age:", self.age)

    def get_info(self):
        print("Coat Color:", self.coat_color)


# Define the JackRussellTerrier class
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def bark(self):
        print("Jack Russell Terrier is barking!")


# Define the Bulldog class
class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def run(self):
        print("Bulldog is running!")


# Create objects and implement the functionalities
dog1 = Dog("Max", 3, "Brown")
dog1.description()
dog1.get_info()
print()

dog2 = JackRussellTerrier("Rocky", 2, "White")
dog2.description()
dog2.get_info()
dog2.bark()
print()

dog3 = Bulldog("Bella", 4, "Fawn")
dog3.description()
dog3.get_info()
dog3.run()
