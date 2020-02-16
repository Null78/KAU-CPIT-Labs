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
