

principle = int(input("Please enter your starting money: "))
interest_rate = float(input("Please enter the interest rate as a decimal with %100 being 1.0: "))
time_period = int(input("Please input the number of years passed with this interest: "))

done = False

while not done:
    result = principle*((1+(interest_rate))**time_period)
    done_check = input("Have you decided to withdraw your money?(y/n): ")
    if done_check == "y":
        done = True
    elif done_check == "n":
        done = False
        time_period += 1
    else:
        print("Please answer with y or n: ")
        done_check = input("Have you decided to withdraw your money?(y/n): ")
print(result)