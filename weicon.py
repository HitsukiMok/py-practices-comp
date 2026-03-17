#Weight Converter (Task 2)

import sys

CONVERT_VALUE = 2.205


while True:

    try:
        weight = float(input("Enter your weight: "))
    except ValueError:
        print("Enter a valid value (Numeric)")
        sys.exit(0)

    #Implemeted an .upper function here to avoid case sensitivity.
    userInput = input("Is the number above in (K)g or (L)bs (K for Kg, L for Lbs): ").upper()

    if userInput == "K":
        converted = weight * CONVERT_VALUE
        print(f"You weigh {converted:.2f} lbs.")
    elif userInput == "L":
        converted = weight / CONVERT_VALUE
        print(f"You weigh {converted:.2f} kg.")
    else:
        print("Please enter a valid option.")

    try:
        cont = int(input("Do you want to try again? \n0 - Yes \n1 - No \n>>"))
    except ValueError:
        print("Unidentified. Please answer properly.")
        sys.exit(0)

    if cont == 1:
        break


print("Exiting program...")