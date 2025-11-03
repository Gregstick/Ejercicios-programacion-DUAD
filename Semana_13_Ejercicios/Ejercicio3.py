from datetime import date

class User:
    def __init__(self, date_of_birth: date):
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        return today.year - self.date_of_birth.year - (
            (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)
        )

def require_adult(func):
    def wrapper(user, *args, **kwargs):
        if user.age < 18:
            print("El usuario debe ser mayor de edad")
        return func(user, *args, **kwargs)
    return wrapper

@require_adult
def register_in_club(user):
    print(f"El usuario se ha registrado. Edad: {user.age}")


adulto = User(date(1997, 12, 19))
print("Edad:", adulto.age)
register_in_club(adulto)

adulto2 = User(date(2015, 11, 11))
print("Edad:", adulto2.age)
register_in_club(adulto2)