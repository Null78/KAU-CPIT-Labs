# problem 1

pound = eval(input("Enter your wight in pounds: ")) * 0.45359237
inch = eval(input("Enter your height in inch: ")) * 0.0254

bmi = pound / (inch) ** 2
print(bmi)


# problem 2

# Get info
invesmentAmount = eval(input("Enter invesment amount: "))
annualInterestRate = eval(input("Enter annual Interest Rate: "))
numberOfYear = eval(input("Enter number of year: "))
# convert
monthlyRate = (annualInterestRate / 100) / 12
numberOfMonths = numberOfYear * 12
# calculate the future invesment
futureInvestment = invesmentAmount * ((1 + monthlyRate) ** numberOfMonths)
# display
print("future value is: ", int(futureInvestment * 100) / 100.0)


# problem 3

# get info
subTotal, gratuityRate = eval(input("Enter sub total and the gratuity rate: "))

# calculate the Eq
x = subTotal * (gratuityRate / 100)
total = subTotal + x

# display
print("the gratuty is", format(x, ".2f"), "and total is ", format(total, ".2f"))


# problem 4

# get info
balance, annualInterestRate = eval(input("Enter balance and annual Interest Rate: "))

# calculate
interest = balance * (annualInterestRate / 1200)
# display
print(interest)



# Extra Q from my doctor

import math
# get s
s = eval(input("Enter s : "))
# calc area
area = (5 * math.pow(s, 2)) / (4 * math.tan(math.pi / 5))
# print area
print(f" the area of the pentagon is {area}")
