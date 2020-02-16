def celsiusToFahrenheit(celsius):
    # Calculate and return the result
    return (9/5) * celsius + 32


def fahrenheitToCelsius(fahrenheit):
    # Calculate and return the result
    return (5 / 9) * (fahrenheit - 32)


def main():
    celsius = 40
    fahrenheit = 120

    # Table header
    print(format("Celsius", "<12s"),
          format("Fahrenheit", "<12s"),
          " | ",
          format("Fahrenheit", ">12s"),
          format("Celsius", ">12s"))
    print("----------------------------------------------------------------")

    while celsius >= 31:
        # Call the functions and print the result formated
        print(format(celsius, "<12d"),
              format(celsiusToFahrenheit(celsius), "<12.2f"),
              " | ",
              format(fahrenheit, ">12d"),
              format(fahrenheitToCelsius(fahrenheit), ">12.2f"))
        celsius -= 1
        fahrenheit -= 10


# Call the main function
main()
