# Get load amount
loan = eval(input("Enter loan amount, for example 120000.95: "))

# Get number of years
years = eval(input("Enter number of years as an integer, for example 5: "))

# Display the header
print()  # Empty line
# Align to the left with width 20 and type string
print(format("Interest Rate", "<20s"), end="")  # Without new line
print(format("Monthly Payment", "<20s"), end="")  # Without new line
print(format("Total Payment", "<20s"))

# Annual Interest Rate %
air = 5

# loop from 5% to 8%
while air <= 8:
    # Calculate the Monthly interest rate
    mir = air / 1200

    # Calculate mothly payment
    monthlyPayment = loan * mir / (1 - (1 / (1 + mir) ** (years * 12)))

    # Calculate total payment
    totalPayment = monthlyPayment * years * 12

    # Display results
    print(format(air, ">5.3f"), "%",
          format(monthlyPayment, "20.2f"),
          format(totalPayment, "20.2f"))

    # Increase annual interset rate by 1/8
    air += 1/8
