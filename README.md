# Reto-3_POO

# Ejericio de clase  
  A continuació se encuentra la solución al ejercicio definiendo una clase
  ``` Python
 class Person:
    def __init__(self, name: str, age:int):
        self.name = name
        self.age = age

    def greet(self):
        print(f"{self.name} te está saludando")

    def is_older_than(self, name: str):
        if self.age > name.age:
            return True
        else:
            return False

person1 = Person("Juan", 30)
person2 = Person("Maria", 27)
person1.greet()
person2.greet()
print(person1.is_older_than(person2))
```
