choice = int(input("Enter 1 for kg --> lbs and 2 for lbs --> kg:"))

if choice == 1:
    kilo = float(input("Please enter kg value:"))
    print(f"The lbs equivalent of {kilo} kilograms is {kilo*2.20462262} lbs.")
elif choice == 2:
    pound = float(input("Please input a lbs value:"))
    print(f"The kg equivalent of {pound} pounds is {pound*0.45359237} kilograms.")
else:
    print("Please input a valid choice.")