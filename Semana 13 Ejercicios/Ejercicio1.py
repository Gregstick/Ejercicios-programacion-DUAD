def print_parameter(func):
    def wrapper(self, *args, **kwargs):
        print(f"Mi nombre es: {self.name}, y tengo: {self.age} años de edad")
        result = func(self, *args, **kwargs)
        return result
    return wrapper



class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age


    @print_parameter
    def adult_person(self):
        if self.age >= 18:
            print(f"{self.name} es mayor de edad")
        else:
            print(f"{self.name} no es mayor de edad")


person_1 = Person("Gregory", 27)
person_1.adult_person()