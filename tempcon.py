# Temperature Converter (Task 3)

KELVIN_CONST = 273.15

import sys

def KtoC (rawVal):
    return rawVal - KELVIN_CONST

def CtoK (rawVal):
    return rawVal + KELVIN_CONST

def FtoC (rawVal):
    return (rawVal - 32) * (5/9)

def CtoF (rawVal):
    return rawVal * (9/5) + 32


print("This is a temperature converter")
tempVal = 0.0
userInput = 0
#To prevent pyLance acting up in the if statement, but this early initialization is not necessary.

while True:

    try:
        tempVal = float(input("Enter the temeperature: "))
        userInput = int(input("Convert to:\n1 - Kelvin to Celcius\n2 - Celcius to Kelvin\n3 - Fahrenheit to Celcius\n4 - Celcius to Fahrenheit\n5 - Fahrenheit to Kelvin\n6 - Kelvin to Fahrenheit\n>> "))

    except ValueError:
        print("Enter a valid number.")
        failVal = input("Do you want to retry? \n 1 - Yes\n 2 - No\n>> ")

        if failVal == "2":
            print("Exiting...")
            sys.exit(0)
        elif failVal == "1":
            continue
        else:
            print("Unidentified value. Exiting program...")
            sys.exit(0)
        #So it won't fail if the user inputs 1.
    
    if userInput == 1:
        result = KtoC(tempVal)
        print(f"The output is: {result:.2f}")
    elif userInput == 2:
        result = CtoK(tempVal)
        print(f"The output is: {result:.2f}")
    elif userInput == 3:
        result = FtoC(tempVal)
        print(f"The output is: {result:.2f}")
    elif userInput == 4:
        result = CtoF(tempVal)
        print(f"The output is: {result:.2f}")
    elif userInput == 5:
        result = FtoC(tempVal)
        finResult = CtoK(result)
        print(f"The output is: {finResult:.2f}")
    elif userInput == 6:
        result = KtoC(tempVal)
        finResult = CtoF(result)
        print(f"The output is: {finResult:.2f}")
    else:
        print("Enter a valid number.")
    
    try:
        cont = int(input("Do you want to input another number?\n1 - No\n2 - Yes\n>> "))
    except ValueError:
        print("Value cannot be deduced. Exiting program....")
        sys.exit(0)
    
    if cont == 1:
        break

print("Exiting Program....")
