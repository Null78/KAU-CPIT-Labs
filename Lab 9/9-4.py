def displayPattern(n):
    for i in range(1, n + 1):

        for j in range(n - i):
            print("  ", end=" ")

        for k in range(i, 0, -1):
            print(format(k, "2d"), end=" ")
        print()


def main():
    # Get input
    n = eval(input("Enter line number: "))

    # Call displayPattern function and pass n
    displayPattern(n)

# Call the main function
main()
