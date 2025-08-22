name = input("Ingrese su nombre")
last_name = input("Ingrese su apellido")
age = int(input("Ingrese su edad"))

if (age <= 2):
    print("De acuerdo a la edad eres un bebé")
elif (age >= 3 and age <= 9):
    print("De acuerdo a la edad eres un niño")
elif (age >= 10 and age <= 12):
    print("De acuerdo a la edad eres un preadolescente")
elif (age >= 13 and age <= 17):
    print("De acuerdo a la edad eres un Adolescente")
elif (age >= 18 and age <= 25):
    print("De acuerdo a la edad eres un adulto joven")
elif (age >= 26 and age <= 59):
    print("De acuerdo a la edad eres un adulto")
elif (age >= 60):
    print("De acuerdo a la edad eres un adulto mayor")
