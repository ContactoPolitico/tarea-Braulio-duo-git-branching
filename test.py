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

