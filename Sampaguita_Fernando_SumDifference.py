# ===============================================================================================
# Name: Thea Margaux M. Fernando
# Section: 8 - Sampaguita
# Sum and Difference Calculator
# ===============================================================================================

number1 = int(input("Enter a number: "))
number2 = int(input("Enter another number: "))

def calculate_sum():
    global number1, number2 # Enter global variable for defined function
    sum = number1 + number2
    print(sum)
calculate_sum()

def calculate_difference():
    global number1, number2
    difference = number1 - number2
    print(difference)
calculate_difference()