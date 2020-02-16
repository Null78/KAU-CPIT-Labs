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