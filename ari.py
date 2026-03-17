import sys

print("This is a basic arithmentic calculator")


# Revisions - instead of printing vals, you should use returns.
# Previous version:
# def add(value1, value2):
    # print(f"The result for {value1} and {value2} is {int(value1) + int(value2)}")


#Remember manipulating with arrays.
#This version doesnt need 2 values therefore its like this:
def add(array = []):
    total = array[0]
    for element in array[1:]:
        total += element
    
    return total

def subtract(array = []):
    total = array[0]
    for element in array[1:]:
        total -= element
    
    return total

def multiply(array = []):
    total = array[0]
    for element in array[1:]:
        total *= element
    
    return total

def divide(array = []):
    total = array[0]
    for element in array[1:]:
        total /= element
    
    return total


#This is the legacy version i initially come up. With the while loop is the final version. o7

# val1 = float(input("Enter first value: "))
# val2 = float(input("Enter second value: "))
 
# print(" 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division")
# operations = int(input("What do you want to do?: "))


# if operations == 1:
    result = add(val1, val2)
    print("The result for " + str(val1) + str(val2) + " is " + str(result))
# elif operations == 2:
    result = subtract(val1, val2)
    print("The result for " + str(val1) + str(val2) + " is " + str(result))
# elif operations == 3:
    result = multiply(val1, val2)
    print("The result for " + str(val1) + str(val2) + " is " + str(result))
# elif operations == 4:
    result = divide(val1, val2)
    print("The result for " + str(val1) + str(val2) + " is " + str(result))
# else:
    print("Please provide a real number.")


# Menu logic here
print("MENU: \nAddition - 1\nSubtraction - 2\nMultiplication - 3\nDivision - 4\nEXIT - 5")

try:
    userInput = int(input("Operation >> "))
except ValueError:
    print("You must input a valid number. Exitting...")
    sys.exit(0)


# The operation loop here
while userInput != 5:
    try:
        valueNum = int(input("How many values >> "))
    except ValueError:
        print("Input a valid number. Exitting...")

    valueToOpe = []
    for i in range(valueNum):
        new_value = float(input("Input a Number >> "))
        valueToOpe.append(new_value)

    if userInput == 1:
        result = add(valueToOpe)
        #would rather use f-strings here, please take note. 
        print("The output is: " + str(result))
    
    elif userInput == 2:
        result = subtract(valueToOpe)
        print("The output is: " + str(result))

    elif userInput == 3:
        result = multiply(valueToOpe)
        print("The output is: " + str(result))

    elif userInput == 4:
        result = divide(valueToOpe)
        print("The output is: " + str(result))
    
    print("\n\nMENU: \nAddition - 1\nSubtraction - 2\nMultiplication - 3\nDivision - 4\nEXIT - 5")

    try:
        userInput = int(input("Operation >> "))
    except ValueError:
        print("You must input a valid number. Exitting...")
        sys.exit(0)


if userInput == 5:
    print("Exiting program...")
    sys.exit(0)
    

