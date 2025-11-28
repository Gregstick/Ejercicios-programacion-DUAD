lista = 'python - variable - funcion - computadora - monitor'

def separated_string(lista):
    splitted_list = lista.split(" - ")
    ordered_list = sorted(splitted_list)
    print(" - ".join(ordered_list))



separated_string(lista)

