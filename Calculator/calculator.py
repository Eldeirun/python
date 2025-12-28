print("Welcome")
operation = input("Please enter an operation (+,-,*,/):")

given = bool(operation)

if given:
     
    a = float(input("Number 1:"))
    b = float(input("Number 2:"))

    if operation == "+":
        print(a+b)
    elif operation == "-":
        print(a-b)
    elif operation == "*":
        print(a*b)
    elif operation == "/":
        if b == 0:
            if a != 0:
                print("No division by 0.")
            else:
                print("Please use a more advanced calculator for calculus.")
        else:
            print(a/b)
    else:
        print("Please re-run calculator and enter a valid operation!")
else:
    print("Please re-run calculator and enter an operation!")