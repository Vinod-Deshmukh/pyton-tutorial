print("#40 Constructors")
class Person:
    def __init__(self,name):
        self.name=name

    def talk(self):
        print(f"Hi, I am {self.name} !")


person=Person("Vinod Deshmukh")
print(person.name)
person.talk()