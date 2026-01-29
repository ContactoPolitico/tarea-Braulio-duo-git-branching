print("test")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = input("Type + to add or - to subtract: ")

if choice == "+":
    result = num1 + num2
    print("Result:", result)

elif choice == "-":
    result = num1 - num2
    print("Result:", result)

else:
    print("Invalid option")

num3 = int(input("Enter first number: "))
num4 = int(input("Enter second number: "))

ans = input("Type x to multiply or / to divide: ")

if ans == "x":
    finish = num3 * num4
    print("Result:", finish)

elif ans == "/":
    finish = num3 / num4
    print("Result:", finish)

else:
    print("Invalid option")
