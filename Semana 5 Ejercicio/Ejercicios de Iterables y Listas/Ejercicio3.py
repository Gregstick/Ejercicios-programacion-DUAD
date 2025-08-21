'Encontre 2 formas de hacerlo'

'1era'
#first_list = [1,2,3,4,5,6,7,8]
#first_list[0], first_list[7] = first_list[7], first_list[0]
#print(first_list)


#second_list = [20,30,40,50,60,80,1290,1080,4000]
#second_list[0], second_list[8] = second_list[8], second_list[0]
#print(second_list)

'2nda'
first_list = [1,2,3,4,5,6,7,8]

primer_elemento = first_list.pop(0)
ultimo_elemento = first_list.pop(-1)

first_list.insert(0, ultimo_elemento)

first_list.append(primer_elemento)


print(first_list)