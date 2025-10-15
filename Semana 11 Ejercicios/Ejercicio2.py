class Person():
    def __init__(self, name):
        self.name = name

class Bus:
    max_passenger = 6

    def __init__(self, max_passenger):
        self.max_passenger = max_passenger
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passenger:
            self.passengers.append(person)
            print(f"{person.name} ha subido al bus")
        else:
            print("El bus está lleno")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} ha bajado del bus")


p1 = Person("Greg")
p2 = Person("Adri")
p3 = Person("John")
p3 = Person("John")
p3 = Person("John")
b1 = Bus(2)
b1.add_passenger(p1)
b1.add_passenger(p2)
b1.add_passenger(p3)
b1.remove_passenger(p1)