# lab 5

# Problem 1
import math

# Get the length from the center to a vertex
r = eval(input("Enter the length from the center to a vertex: "))

# Calculate the length of the side
s = (2 * r) * math.sin(math.pi / 5)

# Calculate the area
area = (3 * math.sqrt(3) / 2) * pow(s, 2)

# Display the result
print("The area of the pentagon is", area)



# Problem 2
# Get the employee's name
name = input("Enter employee's name: ")
# Get the number of hours worked in a week
hours = eval(input("Enter number of hours worked in a week: "))
# Get the hourly pay rate
payRate = eval(input("Enter hourly pay rate: "))
# Calculate the gross Pay
grossPay = hours * payRate
# Get the federal tax withholding rate
fedTaxWithholdingRate = eval(input("Enter federal tax withholding rate: "))
# Get the state tax withholding rate
stateTaxWithholdingRate = eval(input("Enter state tax withholding rate: "))
# Calculate the federal Withholding
fedTaxWithholding = grossPay * fedTaxWithholdingRate
# Calculate the state Withholding
stateTaxWithholding = grossPay * stateTaxWithholdingRate
# Calculate the total deduction
totalDeduction = fedTaxWithholding + stateTaxWithholding
# Calculate the net pay
netPay = grossPay - totalDeduction

# Store, prepare and format the output into a string
out = f"\nEmployee Name: {name}\n" \
        f"Hours Worked: {hours}\n" \
        f"Pay Rate: ${payRate}\n" \
        f"Gross Pay: ${grossPay}\n" \
        f"Deductions:\n" \
        f" Federal Withholding ({fedTaxWithholdingRate * 100}%): {(fedTaxWithholding * 100) / 100.0}\n" \
        f" State Withholding ({stateTaxWithholdingRate * 100}%): {(stateTaxWithholding * 100) / 100.0}\n" \
        f" Total Deduction: ${(totalDeduction * 100) / 100.0}\n" \
        f"Net Pay: {(netPay * 100) / 100.0}"

# Display the result
print(out)



# Problem 3
import math

# get the length of the side
s = eval(input("Enter the side: "))

# calculate the area using the side
area = (5 * pow(s, 2)) / (4 * math.tan(math.pi / 5))

# print the result
print("The area of the pentagon is", area)



# Problem 4
# get the number
num = eval(input("Enter an integer: "))  # 1234

d1 = num % 10  # 4
num = num // 10  # 123

d2 = num % 10  # 3
num = num // 10  # 12

d3 = num % 10  # 2
num = num // 10  # 1

d4 = num  # 1

print("The reversed number is", str(d1) + str(d2) + str(d3) + str(d4))  # 4321


# another way
# get the number
d1, d2, d3, d4 = input("Enter an integer: ")  # 3125
# d1 = 3    d2 = 1    d3 = 2    d4 = 5
print("The reversed number is", d4 + d3 + d2 + d1)  # 5213
