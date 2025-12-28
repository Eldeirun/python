import math

#Find the distance between two lengths at common origin

first = float (input("Please input the first known length:"))
second = float (input("Please input the other known length:"))
angle = float (input("How many pi radians is the angle between the two known lengths:"))


other = math.sqrt((first**2)+(second**2)-(2*first*second*(math.cos(angle*math.pi))))

print (other)