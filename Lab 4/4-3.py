# get info
subTotal, gratuityRate = eval(input("Enter sub total and the gratuity rate: "))

# calculate the Eq
x = subTotal * (gratuityRate / 100)
total = subTotal + x

# display
print("the gratuty is", format(x, ".2f"), "and total is ", format(total, ".2f"))