# Table header
print("--------------------------------------------------------")
# print Miles to the left with width 10 and type string
print(format("Miles", "<10s"),
    # print Kilometers to the right with width 10 and type string
    format("Kilometers", ">10s"),
    # spcae between columns
    "     |     ",
    # print Kilometers to the left with width 10 and type string
    format("Kilometers", "<10s"),
    # print Miles to the right with width 10 and type string
    format("Miles", ">10s"))
print("--------------------------------------------------------")

# Defain counting variables
miles = 1
km = 20

while miles <= 10:
    # Calculate
    miles_to_km = miles * 1.609
    km_to_miles = km / 1.609

    # Display the resault
    # print miles to the left with width 10 and type integer
    print(format(miles, "<10d"),
    # print miles_to_km to the right with width 10 rounded by 3 and type float
    format(miles_to_km, ">10.3f"),
    # spcae between columns
    "     |     ",
    # print km to the left with width 10 and type integer
    format(km, "<10d"),
    # print km_to_miles to the right with width 10 rounded by 3 and type float
    format(km_to_miles, ">10.3f"))

    # Add 1 to miles and 5 to km
    miles += 1
    km += 5
