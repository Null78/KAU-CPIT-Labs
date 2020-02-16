import math

# Get inputs
a, b, c = eval(input("Enter a, b, c: "))

# Calculate the discriminant
discriminant = (b ** 2) - (4 * a * c)

# Check if it's positive -> two roots
if discriminant > 0:
    # Calculate the roots
    root1 = (-b + math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    root2 = (-b - math.sqrt((b ** 2) - (4 * a * c))) / (2 * a)
    # Display the resault
    print("The roots are", root1, "and", root2)

# if it is 0 -> one root
elif discriminant == 0:
    # Calculate the root
    root1 = (-b) / (2 * a)
    # Display the resault
    print("The roots is", root1)

# otherwise, no roots
else:
    print("The equation has no real roots")
