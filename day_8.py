# Pseudo Code:

#     Input: A year (e.g., 2024).
#     Process:
#         If the year is divisible by 400, then it is a leap year.
#         Else if the year is divisible by 100, then it is NOT a leap year.
#         Else if the year is divisible by 4, then it is a leap year.
#         Otherwise, it is NOT a leap year.
#     Output: Print whether the year is a leap year or not.


def check_leap_year(year): # Define a function 
    if year % 400 == 0: # If the year is divisible by 400, it is a leap year.
        return "Leap Year"
    elif year % 100 == 0: # If it is divisible by 100 but not 400, it is not a leap year.
        return "Not a leap year"
    elif year % 4 == 0: # If it is divisible by 4 but not 100, it is a leap year.
        return "Leap Year"
    else: # Otherwise, it is not a leap year.
        return "Not a leap year"

year = int(input("Enter a year: ")) # Asks for user input 

result = check_leap_year(year) # Assigns the return value of that function to the variable result.

print(result) # Outputs results.