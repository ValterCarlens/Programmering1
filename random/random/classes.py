import os
os.system("cls")



class Person:
    def __init__(self, name:str, age:int):
        self.namn = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.namn}({self.age})"

    def greet(self) -> str:
        return "Hej, vad heter du?"
    
    def celebrateBirthday(self) -> None:
        self.age = self.age + 1


person1 = Person("Kalle", 15)
print(person1)
person1.celebrateBirthday()
print(person1)


