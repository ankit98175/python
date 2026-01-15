# task 1: Write a Python program to check whether a number is even or odd.

number = int(input("Enter your number :"))
if number % 2 == 0:
    print("your number is even", number)
else:
    print("your number is odd : ", number)


# Task 2 Sum of Integers from 1 to 50 Using a Loop

sum_of_numbers = 0

for i in range(1, 51):
    sum_of_numbers += i 
print("The sum of integers from 1 to 50 is:", sum_of_numbers)