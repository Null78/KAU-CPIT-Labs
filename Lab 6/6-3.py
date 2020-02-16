# Get package 1 info
p1_size, p1_price = eval(input("Enter weight and price for package 1: "))

# Get package 2 info
p2_size, p2_price = eval(input("Enter weight and price for package 2: "))

# Calculate 1 kg price for package 1
p1 = p1_price / p1_size

# Calculate 1 kg price for package 1
p2 = p2_price / p2_size

# Check the better price and display the output
if p1 < p2:
    print("Package 1 has the better price.")
elif p1 > p2:
    print("Package 2 has the better price.")
else:
    print("Package 1 and Package 2 are the same.")
