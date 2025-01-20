def calculator():
    print("Simple Calculator")
    print("The operators are:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    op=input("choose the operator (1/2/3/4):")
    if op not in ['1','2','3','4']:
        print("Invalid operator")
        print("Please choose the suitable operator")
    num1=float(input("Enter a number:"))
    num2=float(input("enter another number:"))
    if op == '1':
        result = num1 + num2
        print(f"The Addition of {num1} and {num2} is {result}")
    elif op == '2':
        result = num1 - num2
        print(f"The Subtraction of {num1} and {num2} is {result}")
    elif op == '3':
        result = num1 * num2
        print(f"The Multiplication of {num1} and {num2} is {result}")
    elif op == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The Division of {num1} and {num2} is {result}")
        else:
            print("Error: Division by Zero is not allowed.")

calculator()
