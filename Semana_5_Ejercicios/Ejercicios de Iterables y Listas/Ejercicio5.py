numeros = []

for numbers in range(10):
    num = int(input("Ingresa un número: "))
    numeros.append(num)

numero_mas_alto  = numeros[0]

for num in numeros:
    if num > numero_mas_alto:
        numero_mas_alto = num

print(f"Los números que ingresaste son {numeros} Y el más alto es: {numero_mas_alto}")