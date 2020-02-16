amount_of_water = eval(input("Enter amount of water: "))
initialTemp = eval(input("Enter initial temp:  "))
finalTemp = eval(input("Enter final temp: "))
Q = amount_of_water * (finalTemp - initialTemp) * 4184
print(Q)


x1, y1 = eval(input("Enter x1 and y1: "))
x2, y2 = eval(input("Enter x2 and y2: "))

Q = ((x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5

print(Q)