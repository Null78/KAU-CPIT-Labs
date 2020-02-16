def m(i):
    # Calculate
    sum = 0
    for j in range(1, i + 1):
        sum += j / (j + 1)
    # Return the result
    return sum


def main():
    # Header
    print(format("i", "<20s"),
          format("m(i)", "<10s"))

    # Print output
    for i in range(1, 21):
        print(format(i, "<20d"),
              format(m(i), "<20.4f"))


# Call the main function
main()
