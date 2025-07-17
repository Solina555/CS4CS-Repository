# Phase 1
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("Sum:", float(num1) + float(num2))

# Phase 2
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operator (+, -, *, /): ")
if operation == '+':
    print("Result:", float(num1) + float(num2))
elif operation == '-':
    print("Result:", float(num1) - float(num2))
elif operation == '*':
    print("Result:", float(num1) * float(num2))
elif operation == '/':
    if float(num2) != 0:
        print("Result:", float(num1) / float(num2))
    else:
        print("Division by zero is not allowed.")

#Phase 3
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
operation = input("Enter operator (+, -, *, /): ")
redo = True

while redo:
    if operation == '+':
        print("Result:", float(num1) + float(num2))
    elif operation == '-':
        print("Result:", float(num1) - float(num2))
    elif operation == '*':
        print("Result:", float(num1) * float(num2))
    elif operation == '/':
        if float(num2) != 0:
            print("Result:", float(num1) / float(num2))
        else:
            print("Division by zero is not allowed.")
    redo = input("Do you want to calculate again? (yes/no): ").strip().lower() == 'yes'