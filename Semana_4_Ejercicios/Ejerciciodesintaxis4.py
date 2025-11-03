numero_uno = int(input("Ingrese el primer número"))
numero_dos = int(input("Ingrese el segundo número"))
numero_tres = int(input("Ingrese el tercer número"))

if numero_uno >= numero_dos and numero_uno >= numero_tres:
    print(f"El número mayor es: {numero_uno}")
elif numero_dos >= numero_uno and numero_dos >= numero_tres:
    print(f"El número mayor es: {numero_dos}")
else:
    print(f"El número mayor es: {numero_tres}")

