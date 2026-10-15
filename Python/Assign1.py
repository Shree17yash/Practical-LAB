while True:
    try:
        n1 = float(input("Enter the first no: "))
        n2 = float(input("Enter the second no: "))

        print("Enter the operation to be performed:")
        print("1) Add")
        print("2) Subtract")
        print("3) Division")
        print("4) Multiplication")
        print("5) Exponent")
        print("6) Modulus")

        op = int(input("Choose an operation (1-6): "))

        if op == 1:
            print("Result:", n1 + n2)
        elif op == 2:
            print("Result:", n1 - n2)
        elif op == 3:
            if n2 != 0:
                print("Result:", n1 / n2)
            else:
                print("Cannot divide by zero!")
        elif op == 4:
            print("Result:", n1 * n2)
        elif op == 5:
            print("Result:", n1 ** n2)
        elif op == 6:
            if n2 != 0:
                print("Result:", n1 % n2)
            else:
                print("Cannot calculate modulus by zero!")
        else:
            print("Invalid operation! Choose 1-6.")

    except ValueError:
        print("Invalid input! Please enter numbers only.")
