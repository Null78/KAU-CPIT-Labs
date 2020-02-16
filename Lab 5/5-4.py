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




# using for loop
num = input("Enter an integer: ")  # 1234

rev = ""  # declare output variable

# loop same as the input length
for i in range(len(num)):
    # convert num to int
    num = int(num)
    # get the last digit on the right
    d = num % 10
    # add it to the output as a string
    rev = rev + str(d)
    # remove the last digit from num
    num = num // 10

# display the result: 4321
print("The reversed number is", rev)
