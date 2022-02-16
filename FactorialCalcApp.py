#40 days of coding
#November 13th 2021
#Loops Challenge 13: Factorial Calculator App

import math

#Print Welcome Information
print("Welcome to the Factorial Calculator App")

#Get the User input
num=int(input("what number would you like to compute the factorial of: "))

#show your factorial equation
print(str(num) + "! = " , end="")
for i in range(1, num):
  print(str(i), end="*")

print(str(num), end="")

#equation results using the math library
library_result = math.factorial(num)
print("\n\nHere is the result from the math library: ")
print("The factorial of " + str(num) + " is " + str(library_result))

#equation results using your equation 

fact = 1
for i in range(1, num+1):
  fact=fact*i

print("\nHere is the result from my own equation: ")
print("The factorial of " + str(num) + " is " + str(fact))

#print closing statements
print("\nIt is shown twice that " + str(num)+"!"+ " = " + str(library_result))
