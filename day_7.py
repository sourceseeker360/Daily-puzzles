
# Pseudocode for Printing Pyramid Pattern

#     Input:
#         Get the number of rows n for the pyramid pattern.

#     Logic:
#         Loop through each row from 1 to n.
#         For each row:
#             Calculate the number of spaces before the stars. This will be (n - i) where i is the current row number (starting from 1).
#             Calculate the number of stars in the current row. This will be (2 * i - 1) for the i-th row.
#         Print the spaces followed by the stars for each row.

#     Output:
#         Print the pyramid pattern.

def print_pyramid(n):
    for i in range(1, n + 1):  # Loop through each row
        # Calculate the number of spaces before the stars
        spaces = n - i
        # Calculate the number of stars in the current row
        stars = 2 * i - 1
        # Print spaces
        print(' ' * spaces, end='')
        # Print stars
        print('*' * stars)

# Input the number of rows
n = int(input("Enter the number of rows: "))
print_pyramid(n)
