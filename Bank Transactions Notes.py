# Programmer: Josiah Fuller
# Date: 10/13/2021
# Program: Bank Transaction

"""This program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements and refresh our Comparison & Logical Operators"""

print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their first and last names using Variables

def setupAccount():

    firstName = input("Enter your first name, please: ")

    lastName = input("Enter your last name, please: ")

    print("\nWelcome to Cash-R-Us,", firstName, lastName + ",we will now set up a security pin on your account.\n")

    # Set up a PIN - Personal Identification Number

    pinNum = input("Please choose a four-digit Personal Identification Number: ")

    print("\nThank You," + firstName + ", we see that you set your PIN to " + pinNum)

setupAccount()






print("\nWould you like to make a transaction through our Automated Teller Machine?")