

try:
    choice1 = int(input("From what unit to convert from? (1 for C, 2 for F and 3 for K):"))
    choice2 = int(input("To what unit to convert to? (1 for C, 2 for F and 3 for K):"))

    
    value = float(input("What degree?:"))

    if choice1 == 1:
        if choice2 == 1:
            print(f"{value}C")
        elif choice2 == 2:
            print(f"Roughly {(value*2)+30}F")
        elif choice2 == 3:
            print(f"{value+273.15}K")
        else:
            print("Invalid choice.")
    elif choice1 == 2:
        if choice2 == 1:
            print(f"Roughly {(value-30)/2}F")
        elif choice2 == 2:
            print(f"{value}F")
        elif choice2 == 3:
            print(f"Roughly {((value-30)/2)+273.15}")
        else:
            print("Invalid choice.")
    elif choice1 == 3:
        if value < 0:
            print("Below absolute zero")
        else:

            if choice2 == 1:
                print(f"{value-273.15}C")
            elif choice2 == 2:
                print(f"Roughly {((value-273.15)*2)+30}")
            elif choice2 == 3:
                print(f"{value}K")
            else:
                print("Invalid choice.")
    else:
        print("Invalid choice.")

except (ValueError, TypeError) as error:
    print(f"Error {error} has occurred.")


finally:
    print("Program successfully or unsuccessfully completed")
