def main():
    expression= input("expression:")
    result = eval(expression)
def calc(result):
    result = result.split()
    if len(result) != 3:
        raise ValueError("Invalid expression: expression must contain two numbers and an operator")
    
    a = int(result[0])
    b = int(result[2])
    operator = result[1]
    
    if operator == "+":
        return float(a + b)
    elif operator == "-":
        return float(a - b)
    elif operator == "*":
        return float(a * b)
    elif operator == "/":
        return float(a / b)
    else:
        raise ValueError("Unrecognized operator: expression must use one of '+', '-', '*', or '/'")
main()