#Ejercicio 3 de Semana 6

def sum_of_numbers(numbers):
    sum_all_numbers = 0
    for n in numbers:
        sum_all_numbers += n
    return sum_all_numbers


list_of_numbers = [50, 5004, 5069, 44, 1080, 90, 80, 99999, 1333444]
print(f'{list_of_numbers} ----> {sum_of_numbers(list_of_numbers)}')

#Ejercicio 4 de Semana 6

def string(parametro):
    cadena_invertida = parametro[::-1]
    return f"{parametro}----> {cadena_invertida}"


resultado = string("Hola mundo")
print(resultado)


#Ejercicio 5 de Semana 6

def string_upper_and_lower_case():
    mayusculas = 0
    minusculas = 0
    for texto in ("I love Nación Sushi"):
        if texto.isupper():
            mayusculas += 1
        else:
            minusculas += 1
    print(f'I love Nación Sushi ---> There is {mayusculas} upper cases and {minusculas} lower cases')


string_upper_and_lower_case()


#Ejercicio 6 de Semana 6

lista = 'python - variable - funcion - computadora - monitor'

def separated_string(lista):
    splitted_list = lista.split(" - ")
    ordered_list = sorted(splitted_list)
    print(" - ".join(ordered_list))



separated_string(lista)


#Ejercicio 7 de Semana 6

def prime_numbers(lista_de_numeros):
    numeros_primos = []
    for n in lista_de_numeros:
        if n < 2:
            continue
        es_primo = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break
        if es_primo:
            numeros_primos.append(n)
    print(numeros_primos)


lista_de_numeros = [1, 4, 6, 7, 13, 9, 67]
print(f'{lista_de_numeros} ---->'), prime_numbers(lista_de_numeros)