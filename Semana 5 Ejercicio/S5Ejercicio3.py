list_of_keys = ["years_in_the_company", "number_of_illnesses"]
employee = {"name": "Scottie", "email": "scottiepippen@gmail.com", "age": 35, "years_in_the_company": 5, "number_of_illnesses": 3}

deleted_item_1 = employee.pop('years_in_the_company')
deleted_item_2 = employee.pop('number_of_illnesses')
print(employee)
print(f'Deleted item 1: {deleted_item_1}')
print(f'Delete item 2: {deleted_item_2}')