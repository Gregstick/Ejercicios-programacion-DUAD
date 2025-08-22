a_list = [1,2,3,4,5,6,7,8,9]

pair = []

for num in a_list:
    if num % 2 == 0:
        pair.append(num)

a_list = pair

print(a_list)