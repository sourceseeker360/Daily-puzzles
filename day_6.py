
# Calculate the sum of all numbers in a list.


# Pseudocode:

#     Define a function sum_of_list(numbers):
#         Input: A list of numbers called numbers.
#         Output: The total sum of all numbers in the list.
#     Initialize a variable total_sum to 0.
#     Loop through each number in numbers:
#         Add the number to total_sum.
#     Return total_sum.
#     Test the function with an example list like [1, 2, 3, 4, 5].
#     Print the result.



def sum_of_list(numbers):
    # Initialize the total sum to 0
    total_sum = 0 

    # Loop through each number in the list
    for number in numbers:
        total_sum += number
    # Return the total sum
    return total_sum
# Test the function with an example list
example_list = [1,2,3,4,5]
result = sum_of_list(example_list)

# Print the result
print(f"The sum of the list {example_list} is: {result}")
