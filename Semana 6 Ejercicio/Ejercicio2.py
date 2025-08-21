def inside_variable_function():
    inside_variable = "Esta es la variable local"
    print(inside_variable)


inside_variable_function()


outside_variable = "Esta es la variable globlal"


def outside_variable_function():
    print(outside_variable)


outside_variable_function()