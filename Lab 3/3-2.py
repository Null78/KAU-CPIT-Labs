minutes = eval(input("Enter the number of minutes: "))
number_of_days = minutes // 1440
number_of_years = number_of_days // 365
print(f"{minutes} is {number_of_years} years and {number_of_days % 365} days")