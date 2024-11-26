
def sum(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def division(a, b):
    return a / b 
def multiplication(a, b):
    return a * b
def power(a, b):
    return a ** b
def quotient(a, b):
    return a % b
def rest(a, b):
    return a // b
def switch(operation, a, b):
    dictionary = {
        "+": sum,
        "-": subtraction,
        "/": division,
        "*": multiplication,
        "**": power,
        "%": quotient,
        "//": rest,
    } 
    function = dictionary.get(operation, lambda a, b: "Operation not found")
    return function(a, b)

while True: 
    a = float(input("Enter the value of A (Enter 0 to exit): "))
    if a == 0:
        print("See you soon!")
        break
    operation = input("Select an operation ( +, -, /, *, **, %, %, //): ")
    b = float(input("Enter the value of B (0 to exit): "))
    if b == 0:
        print("See you soon!")
        break
    print(switch(operation, a, b))