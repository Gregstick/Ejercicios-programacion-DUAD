def bubble_sort(list_to_sort):
    for outer_index in range(0, len(list_to_sort) -1): # 0(n)
        has_made_changes = False
        for index in range(0, len(list_to_sort) -1 -outer_index): # 0(n^2)
            current_element = list_to_sort[index] # O(1)
            next_element = list_to_sort[index + 1] # O(1)

            print(f'-- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, siguiente elemento: {next_element}') # 0(1)

            if current_element > next_element: # O(1)
                print("El elemento actual es mayor al siguiente. Intercambiandolos...") # O(1)
                list_to_sort[index] = next_element # O(1)
                list_to_sort[index + 1] = current_element # O(1)
                has_made_changes = True

        if not has_made_changes:
            return # O(1)

my_test_list = [18, -11, 68, 6, 32, 53, -2] # O(1)
bubble_sort(my_test_list) # O(n)

print(my_test_list) # O(1)