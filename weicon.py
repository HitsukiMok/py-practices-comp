#Weight Converter (Task 2)

import sys

CONVERT_VALUE = 2.205

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