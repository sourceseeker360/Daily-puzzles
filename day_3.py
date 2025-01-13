# Puzzle of the Day: Count the Vowels

# Problem: Write a program that takes a string as input 
# and counts the number of vowels in that string. 
# For this puzzle, consider the vowels to be 
# "a", "e", "i", "o", "u" (both lowercase and uppercase).

# Pseudocode:

#     Start
#     Initialize a variable vowel_count to 0.
#     Take input from the user for the string.
#     Loop through each character of the string:
#         If the character is a vowel (a, e, i, o, u, A, E, I, O, U):
#             Increment vowel_count by 1.
#     After the loop ends, print vowel_count to display the total number of vowels in the string.
#     End


vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # Vowels to check in string.
user_input = input('Enter a String: ') # User inputs string.
vowel_count = 0 # Setting counter for loop

for char in user_input: # looping through user input
    if char in vowels: # Checking each character in string for vowel.
        vowel_count += 1 # Whenever a vowel is found increment to eventually exit for loop

print(f"Vowel count: {vowel_count}") # output results