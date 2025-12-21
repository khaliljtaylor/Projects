print("***Welcome to the simple calculator program by Khalil Taylor***")
print("Perform the operations of add, subtract, multiply, divide and remainder.")
print("\nSelect Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")

def main():
    choice = getChoice()
    if choice in ['1']:
        additionResult = addition()
        print("The result is: ", additionResult)
    if choice in ['2']:
        subtractionResult = subtraction()
        print("The result is: ", subtractionResult)
    if choice in ['3']:
        multiplicationResult = multiplication()
        print("The result is: ", multiplicationResult)
    if choice in ['4']:
        divisionResult = division()
        print("The result is: ", divisionResult)
    if choice in ['5']:
        remainderResult = remainder()
        print("The result is: ", remainderResult)
    exit_continue()
    

def getChoice():
    choice = input("\nEnter choice: ")
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid input. Please select a valid operation.")
        return getChoice()
    return choice

def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a + b

def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a - b

def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a * b

def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return division()
    return a / b

def remainder():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
        return remainder()
    return a % b

def exit_continue():
    decision = input("\nDo you wish to exit Y or N:")
    if decision in ['Y', 'y']:
        print("Thank you for using the calculator program. Goodbye!")
        exit()
    elif decision in ['N', 'n']:
        main()
    else:
        print("Invalid input. Please enter Y or N.")
        exit_continue()


main()