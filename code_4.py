#Part 1
print(7+5)
print("\n")

#Part 2
name = input("Enter your name: ")
print(f"Hello, {name}!")
print("\n")

# Part 3
num = int(input("Enter a number: "))
if num%2 == 0:
    print(f"Even")
else:
    print(f"Odd")
print("\n")

# Part 4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}.")
elif num1 < num2:
    print(f"{num1} is less than {num2}.")
elif num1 == num2:
    print(f"{num1} is equal to {num2}.")
print("\n")

# Part 5
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("C")