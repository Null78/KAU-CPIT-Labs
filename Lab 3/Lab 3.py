# Problem 1

pi = 3.14159
radius, length = eval(input(" Enter radius and length: "))

area = radius * radius * pi
volume = area * length  # radius is wrong the right answer is area * length
print(area)
print(volume)


# Problem 2

minutes = eval(input("Enter the number of minutes: "))
number_of_days = minutes // 1440
number_of_years = number_of_days // 365
print(f"{minutes} is {number_of_years} years and {number_of_days % 365} days")


# Problem 3

Celsius = eval(input("Enter the degree in Celsius: "))
fahrenheit = (9/5) * Celsius + 32
print(fahrenheit)


# Problem 4

amount_of_water = eval(input("Enter amount of water: "))
initialTemp = eval(input("Enter initial temp:  "))
finalTemp = eval(input("Enter final temp: "))
Q = amount_of_water * (finalTemp - initialTemp) * 4184
print(Q)


x1, y1 = eval(input("Enter x1 and y1: "))
x2, y2 = eval(input("Enter x2 and y2: "))

Q = ((x2 - x1) ** 2 + (y2 - y1) ** 2 ) ** 0.5

print(Q)
