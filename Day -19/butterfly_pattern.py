def print_butterfly(rows):
    for i in range(1, rows + 1):
        for j in range(1, 2 * rows + 1):
            if j <= i or j > 2 * rows - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    for i in range(rows, 0, -1):
        for j in range(1, 2 * rows + 1):
            if j <= i or j > 2 * rows - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Example usage
rows = 4 # Change this value to the desired number of rows
print_butterfly(rows)
