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

    print("\nWelcome to Cash-R-Us,", firstName, lastName + ", we will now set up a security pin on your account.\n")

    # Set up a PIN - Personal Identification Number

    pinNum = input("Please choose a four-digit Personal Identification Number: ")

    print("\nThank You," + firstName + ", we see that you set your PIN to " + pinNum)






































































def makeATransaction():
    print("\nWould you like to make a transaction through our Automated Teller Machine?")

    #Asks if the user wants to write yes or no
    atmBoolean = input("(write yes or no): ").lower()

    #Checks if the user types yes
    if (atmBoolean == "yes" or "yep" or "yessir"):
        print("\n*****************************************\nyoyoyoyoyoyoyoyo ur coolz\n")
        #Checks if the user types no
    elif (atmBoolean == "no" or "nope"):
        print("\n*****************************************\nThank you, have a great day!")
        #Check if the user has written anything else besides yes or no
    else:
        print("\n*****************************************\nNot a valid term")
        #If the user types stuff other than a yes or no, then restart the program and give the user a chance to retype yes or no
        makeATransaction()


        
















































































































































#Calls the functions SetupAccount and makeATransaction
setupAccount()
makeATransaction()