"""Choose a program to build:

- Even or Odd Checker: Enter a number, and the program tells you if it’s even or odd using % and conditionals.

- Simple Chatbot: Respond to basic greetings or phrases using if/elif logic.

1. Write out the pseudocode for your chosen task in a docstring.
2. Document the description of the code with comments
3. Name your objects with the snake case format.
4. Use the various data types to store your data in the named variable.
5. Use built-in functions at your discretion e.g. print() , input()
"""
#######################################################################################################################

"""Even or Odd Checker:
request input from the user
save input in a variable named number
check if the number is even with division
output odd if there is a remainder
or output even if there is not a remainder
"""

# request input from the user
number = input("Enter a number: ")

# cast the number to an integer
cast_number = int(number)

# use conditional statements to check for even or odd input
# use modulus to check for a remainder after division by 2
# print out even if there is no remainder
# print out odd if there is a remainder
if cast_number % 2 == 0:
    print("Even")

else:
    print("Odd")

######################################################################################################################

"""Simple Chatbot:
request the user to input an hour between 1 and 24
output good morning if the time is greater than or equal to 1 and less than 12  
output good afternoon if the time is greater than or equal to 12 and less than 18
output good evening if the time is greater than or equal to 18 and less than or equal to 24
"""

# request the user to input an hour between 1 and 24
time = input("Enter the time as an hour between 1 and 24: ")

# cast the time to an integer
cast_time = int(time)

# check if the time is in the morning
if 1 <= cast_time < 12:
    print("Good morning!")

# check if the time is in the afternoon
elif 12 <= cast_time < 18:
    print("Good afternoon!")

# check if the time is in the evening
elif 18 <= cast_time <= 24:
    print("Good evening!")

# check for an invalid input
else:
    print("Invalid time")

