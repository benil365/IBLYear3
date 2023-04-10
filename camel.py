def camel_to_snake(camel_case):
    """
    The function converts a string in camel case to snake case.
    
    :param camel_case: The input string in camel case format that needs to be converted to snake case
    :return: The function `camel_to_snake` returns a string in snake_case format, which is converted
    from the input string in camelCase format.
    """
    snake_case = ""
    for i, char in enumerate(camel_case):
        if i == 0:
            snake_case += char.lower()
        elif char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    return snake_case

# This code prompts the user to enter a variable name in camel case, then converts it to snake case
# using the `camel_to_snake` function, and finally prints the variable name in snake case.
camel_case_var = input("Enter variable name in camel case: ")
snake_case_var = camel_to_snake(camel_case_var)
print("Variable name in snake case: ", snake_case_var)