import math

# Get the length from the center to a vertex
r = eval(input("Enter the length from the center to a vertex: "))

# Calculate the length of the side
s = (2 * r) * math.sin(math.pi / 5)

# Calculate the area
area = (3 * math.sqrt(3) / 2) * pow(s, 2)

# Display the result
print("The area of the pentagon is", area)
