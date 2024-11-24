# Ejercicio clase 6

  A continuació se encuentra la solución al ejercicio definiendo una clase
  ``` Python
class Person:
    specie = "Human"
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"{self.name} te está saludando")

    def is_older_than(self, other_person: 'Person'):
        if self.age > other_person.age:
            return True
        else:
            return False

person1 = Person("Juan", 30)
person2 = Person("Maria", 27)
print(Person.specie)
person1.greet()
person2.greet()
print(person1.is_older_than(person2))
```
