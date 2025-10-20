def verification_decorator(func):
    def wrapper(*args, **kwargs):
        self = args[0]
        for number in (self.number1, self.number2):
            if not isinstance(number, (int, float)):
                print(
                    "Este no es un número, por favor ingresa un valor válido"
                )
                return
        return func(*args, **kwargs)
    return wrapper


class Two_numbers:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    @verification_decorator
    def sum_of_two_numbers(self):
        sum_numbers = self.number1 + self.number2
        print(f"Este es el resultado de la suma: {sum_numbers}")


sum1 = Two_numbers(5, 10)
sum1.sum_of_two_numbers()

sum2 = Two_numbers("g", "C")
sum2.sum_of_two_numbers()