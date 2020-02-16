import math

# get the length of the side
s = eval(input("Enter the side: "))

# calculate the area using the side
area = (5 * pow(s, 2)) / (4 * math.tan(math.pi / 5))

# print the result
print("The area of the pentagon is", area)
