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