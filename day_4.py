# Write a program that takes a sentence as input and identifies the longest word in 
# the sentence.

# Pseudo Code:

# 1. Define a function called find_longest_word that accepts
# a string (sentence) as input

# 2. split the sentence into a list of words using the split() function.

# 3. Initialize a variable longest_word to an empty string.

# 4. Loop through each word in the list. 

# 5. Return the longest_word

# 6. Test the function with a sample sentence and print the results.


def find_longest_word(sentence):
    words = sentence.split()
    longest_word = ""
    for word in words:
        if len(word) > len(longest_word):  # Compare the length of the current word to the longest_word
            longest_word = word

    return longest_word  # Return the longest word

# Prompt the user to input a sentence
sentence = input("Enter a sentence: ")
print("Longest word:", find_longest_word(sentence))
