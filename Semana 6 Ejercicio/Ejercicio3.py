def sum_of_numbers(numbers):
    sum_all_numbers = 0
    for n in numbers:
        sum_all_numbers += n
    return sum_all_numbers


list_of_numbers = [50, 5004, 5069, 44, 1080, 90, 80, 99999, 1333444]
print(f'{list_of_numbers} ----> {sum_of_numbers(list_of_numbers)}')








