# Pattern 1
print("\nPattern 1\n")
for i in range(1, 7):
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# Pattern 2
print("\nPattern 2\n")
for i in range(6, 0, -1):
    for k in range(1, i + 1):
        print(k, end=" ")
    print()

# Pattern 3
print("\nPattern 3\n")
for i in range(1, 7):

    for j in range(6 - i):
        print(" ", end=" ")

    for k in range(i, 0, -1):
        print(k, end=" ")
    print()

# Pattern 4
print("\nPattern 4\n")
for i in range(6, 0, -1):

    for j in range(6 - i):
        print(" ", end=" ")

    for k in range(1, i + 1):
        print(k, end=" ")
    print()
