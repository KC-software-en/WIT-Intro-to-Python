"""Build a simple contact book or shopping list using lists and dictionaries.

1. Write out the pseudocode for your chosen task in a docstring.
2. Document the description of the code with comments
3. Name your objects with the snake case format.
4. Use the various data types to store your data in the named variable.
5. Use a list or dictionary to store your data.
"""

"""This is a docstring. Like comments, when Python runs your code it will not pick up a docstring as code.
Read more: https://peps.python.org/pep-0008/#documentation-strings
"""

"""store the shopping list in a variable named groceries
save the grocery items as the value for the groceries variable
print out the grocery list variable
"""

# set a variable named shopping_list
# enter the shopping_list as a string data type
shopping_list = ["bread", "milk", "sugar", "pasta"]

# print out the grocery list
print(shopping_list)

"""store the contact book in a variable named contact_book 
save the contact details as the value in contact_book
print out the contact book
"""

# set a variable named contact book
# create a dictionary to store contact details for a person
contact_book = {
    "name": "Lola Privet",
    "phone number": "0827567585",
    "address": "21 Milky Lane, Canon, 8002",
    "married": True,
    "kids": 0
}

# print out the contact book
print(contact_book)

