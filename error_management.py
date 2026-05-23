def divide_numbers():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    try:
        result=a/b
        print("The result is: ",result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError as e:
        print("Error: Invalid input. Please enter numeric values.")
divide_numbers()