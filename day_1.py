
# Problem:

# Find the largest of three numbers.

# Pseudocode:

# 1. Take three numbers as input.
# 2. Compare the numbers using if-else or max function.
# 3. Output the largest number.


num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))
num_3 = int(input('Enter third number: '))

largest = max(num_1,num_2,num_3)

print('The largest number is: ', largest)