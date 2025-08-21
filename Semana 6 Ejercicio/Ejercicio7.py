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


