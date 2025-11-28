first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']


index = 1

for word in second_list:
    if index < len(first_list):
        first_list.insert(index, word)
    else:
        first_list.append(word)
    index += 2

for i in range(0, len(first_list), 2):
    print(first_list[i], first_list[i+1])
