print("#41 Inheritance")
class Mammal:
    def walk(self):
        print("walk")

class Dog(Mammal):
    def run(self):
        print("run!")

class Cat(Dog):
    pass
dog=Dog()
cat=Cat()
dog.walk()
cat.walk()
dog.run()
cat.run()