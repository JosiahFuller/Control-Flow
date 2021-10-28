# Programmer: Josiah Fuller
# Date: 10/13/2021
# Program: Bank Transaction

"""This program simulates an ATM utilizing If, Elif, & Else statements
Nesting If statements and refresh our Comparison & Logical Operators"""



print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

command1 = input("If you would like to log into your account, press 1.\n If you would like to sign up for a new account, press2: ")
if (command1 == "2"):
    print ("You have chosen to set up a new Account\n")
elif (command1 == "1"):
    print("Please sign into your account")
else:
    print("That is not a valid input")







print("Welcome to Cash-R-Us Bank\nLet's take a moment to set up your account.\n")

# Set up account by asking users for their first and last names using Variables


firstName = input("\nEnter your first name, please: ")
lastName = input("Enter your last name, please: ")
print("\nWelcome to Cash-R-Us,", firstName, lastName + ", we will now set up a security pin on your account.\n")

# Set up a PIN - Personal Identification Number

pinNum = input("Please choose a four-digit Personal Identification Number: ")

print("\nThank You, " + firstName + ", we see that you set your PIN to " + pinNum)














def setupAccount():

    #Asks the user for their first name
    firstName = input("Enter your first name, please: ")

    #Asks the user for their last name
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
        #This part of the [rogram asks users to perform a transaction through the ATM Machine
        print("\n*****************************************\nyoyoyoyoyoyoyoyo ur coolz\n")
        print("Please insert your ATM card in the card slot\n")
        print("Welcome to Toys-4-U,", firstName, lastName, "\n")
        userPIN = input("What is your 4-digit PIN?: ")

        if (userPIN == pinNum):
            print("Thank you for entering your PIN. I now have your precious data.")
            userBalance = 6,000,000,000,000,000,000,000
            print("Hello,", firstName, "Your user balance is: " + str(userBalance))

            #Ask users what type of transaction they want, withdrawal or deposit
            typeOfTransaction = input("\n Would you like to make a withdrawal,  deposit?, or check your balance?: ").lower()
            if (typeOfTransaction == "withdrawal"):
                print("\nYou have chosen to withdraw cash, sucka!\n")
                withdrawalAmount = int(input("How much money do you want?: "))
                userBalance -= withdrawalAmount
                print("\nYour balance is now $" + str(userBalance), ", jerk. Here's your stupid money.")
                
            elif (typeOfTransaction == "deposit"):
                print("\nYou have chosen to give me money, sucker!\n")
                depositAmount = int(input("How much money do you want to give me?: "))
                userBalance -= depositAmount
                print("\nYour balance is now $" + str(userBalance), ", my good sir. Thank you for feeding me.")
            
            elif (typeOfTransaction == "balance"):
                print("Here's ur account balance, asshole:", str(userBalance))
                
            else:
                print("WHYYYYY")

        else:
            print("Silly goose, that was the wrong PIN. Do it again and I will haunt your dreams.\n Have a great day!")


    elif (atmBoolean == "no" or "nope"):
        print("\n*****************************************\nThank you, have a great day!")


        #Check if the user has written anything else besides yes or no
    else:
        print("\n*****************************************\nNot a valid term")
                #If the user types stuff other than a yes or no, then restart the program and give the user a chance to retype yes or no
        makeATransaction()








#Calls the function makeATransaction


#Calls the functions SetupAccount and makeATransaction
setupAccount()
makeATransaction()


