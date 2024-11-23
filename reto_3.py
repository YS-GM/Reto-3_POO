class Person:
    specie = "Human" # Atributo de clase compartido por todas las instacias
    def __init__(self, name: str, age:int):
        self.name = name # Atributo de instancia para el nombre de la persona
        self.age = age # Atributo de instancia para la edad de la persona

    def greet(self):
        print(f"{self.name} te está saludando") # Método de saludo

    def is_older_than(self, other_person: 'Person'):
       # Compara la edad de la instancia actual con la edad de otra instancia
        if self.age > other_person.age:
            return True
        else:
            return False

# Creando instancias de Person
person1 = Person("Juan", 30)
person2 = Person("Maria", 27)

# Accediendo a los atributos y métodos de las instancias
print(Person.specie)
person1.greet()
person2.greet()
print(person1.is_older_than(person2))

