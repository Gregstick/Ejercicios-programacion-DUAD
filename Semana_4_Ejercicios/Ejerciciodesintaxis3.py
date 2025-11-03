numero = int(input("Ingresa y adivina el número secreto"))
import random
numero_secreto = random.randint(1, 10)


while numero != numero_secreto:
    print("Intentalo de nuevo")
    numero = int(input("Ingresa y adivina el numero secreto: "))

print(f"Adivinaste, {numero_secreto} es el número secreto")