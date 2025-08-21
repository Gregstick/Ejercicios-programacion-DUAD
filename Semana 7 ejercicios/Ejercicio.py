def option_1_addition(current_number):
    while True:
        entry = input("Ingrese el número a sumar, 'C' para reiniciar o escribe 'M' para ir al menú ")

        if entry.upper() == "C":
            current_number = int(input("Reiniciado. Ingrese nuevo número: "))
            continue

        if entry == "M":
            return current_number


        try:
            number_to_add = int(entry)

            if number_to_add < 0:
                print("El número debe ser cero o mayor.")
                continue

            current_number += number_to_add
            print(f"Resultado actual: {current_number}")

        except ValueError:
            print("Por favor ingrese un número válido o 'C' para reiniciar ")



def option_2_subtraction(current_number):
    while True:
        entry = input("Ingrese el número a restar, 'C' para reiniciar o escribe 'M' para ir al menú ")


        if entry.upper() == "C":
            current_number = int(input("Reiniciado. Ingrese nuevo número: "))
            continue

        if entry == "M":
            return current_number


        try:
            number_to_subtract = int(entry)

            if number_to_subtract <= 0:
                print("El número debe ser mayor que cero.")
                continue

            current_number -= number_to_subtract
            print(f"Resultado actual: {current_number}")

        except ValueError:
            print("Por favor ingrese un número válido o 'C' para reiniciar ")



def option_3_multiplication(current_number):
    while True:
        entry = input("Ingrese el número a multiplicar, 'C' para reiniciar o escribe 'M' para ir al menú ")

        if entry.upper() == "C":
            current_number = int(input("Reiniciado. Ingrese nuevo número: "))
            continue

        if entry == "M":
            return current_number


        try:
            number_to_multiply = int(entry)

            if number_to_multiply <= 0:
                print(f"Resultado actual: {current_number}")
                continue

            current_number *= number_to_multiply
            print(f"Resultado actual: {current_number}")

        except ValueError:
            print("Por favor ingrese un número válido o 'C' para reiniciar ")


def option_4_division(current_number):
    while True:
        entry = input("Ingrese el número a dividir, 'C' para reiniciar o escribe 'M' para ir al menú ")

        if entry.upper() == "C":
            current_number = int(input(f"Reiniciado. Ingrese nuevo número: "))
            continue

        if entry == "M":
            return current_number


        try:
            number_to_divide = int(entry)

            if number_to_divide <= 0:
                print(f"Resultado actual: {current_number}")
                continue

            current_number /= number_to_divide
            print(f"Resultado actual: {current_number}")

        except ValueError:
            print("Por favor ingrese un número válido o 'C' para reiniciar ")




def calculator():
    try:
        current_number = int(input("Ingrese un número: "))
    except ValueError:
        print("Por favor ingrese un número válido ")
        return
    
    while True:
        operator = input(f"Elige y escribe la operación que quieres realizar:\n  + →Si desea hacer una suma\n  - →Si desea hacer una resta\n  * →Si desea hacer una multiplicación\n  / →Si desea hacer una división\n  S → Salir\n  C →Si desea limpiar el resultado\n  Resultado actual: {current_number}\n Ingrese operación: " )

        try:

            if operator == "+":
                current_number = option_1_addition(current_number)

            elif operator == "-":
                current_number = option_2_subtraction(current_number)

            elif operator == "*":
                current_number = option_3_multiplication(current_number)

            elif operator == "/":
                current_number = option_4_division(current_number)

            elif operator.upper() == "S":
                print("Saliendo. Resultado final: ", current_number)
                break

            elif operator.upper() == "C":
                current_number = int(input(f"Reiniciado. Ingrese nuevo número: "))
                continue

            else:
                print("Por favor ingrese una de las opciones válidas dadas ")


        except ValueError:
            print("Por favor ingrese un valor válido ")




calculator()