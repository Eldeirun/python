import time

duration = int(input("Please enter a duration in seconds:"))
reverse = input("Reversed or not(y/n):")

if reverse == "y":
    for i in reversed(range(1,duration+1)):
        print(i)
        time.sleep(1)
else:
    for i in range(1,duration+1):
        print(i)
        time.sleep(1)
