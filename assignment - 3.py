# ----------------------Task 1: Factorial Calculation----------------------

factorial = int(input("Enter a number to compute its factorial: "))
if factorial == 0:
    print("The factorial of 0 is 1")
else:
    result = 1
    for i in range(1, factorial + 1):
        result *= i
    print("The factorial of", factorial, "is:", result)
    
    
# -----------------Task 2: Square Root, Natural Logarithm, and Sine Calculation----------------------

import math

number = float(input("Enter a number to find its square root: "))
square_root = math.sqrt(number)
print("The square root of", number, "is:", square_root)
natural_logarithm = math.log(number)
print("The natural logarithm of", number, "is:", natural_logarithm)
sine_value   = math.sin(number)
print("The sine of", number, "is:", sine_value) 