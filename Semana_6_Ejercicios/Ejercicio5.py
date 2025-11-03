def string():
    mayusculas = 0
    minusculas = 0
    for texto in ("I love Nación Sushi"):
        if texto.isupper():
            mayusculas += 1
        else:
            minusculas += 1
    print(f'I love Nación Sushi ---> There is {mayusculas} upper cases and {minusculas} lower cases')


string()

#texto = string("I love Nación Sushi")
#print(f'{texto}---> There is {mayusculas} upper cases and {minusculas} lower cases')