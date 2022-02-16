#40 days of coding
#November 4th 2021
#Basic Data Types Challenge 5: Multiplication / Exponent Table App. 

title="Welcome to the Multiplication / Exponent Table App"
print(title)

#Gather the Users Name
name=input("What is your name, ")

#Gather user data
num=float(input("What number would you like to work with: ", ))

#Multilpication Table Equations
print("\n")
print("Multiplication Table for : "+ str(num))
print("\n")
print("\t 1.0 * " + str(num) + " = " + str(round(1*num, 4)))
print("\t 1.0 * " + str(num) + " = " + str(round(2*num, 4)))
print("\t 3.0 * " + str(num) + " = " + str(round(3*num, 4)))
print("\t 4.0 * " + str(num) + " = " + str(round(4*num, 4)))
print("\t 5.0 * " + str(num) + " = " + str(round(5*num, 4)))
print("\t 6.0 * " + str(num) + " = " + str(round(6*num, 4)))
print("\t 7.0 * " + str(num) + " = " + str(round(7*num, 4)))
print("\t 8.0 * " + str(num) + " = " + str(round(8*num, 4)))
print("\t 9.0 * " + str(num) + " = " + str(round(9*num, 4)))

#Exponent Table Equations
print("\n")
print("Exponent Table for : "+ str(num))
print("\n")
print("\t" + str(num) + "** 1 = " + str(round(num**1,4)))
print("\t" + str(num) + "** 2 = " + str(round(num**2,4)))
print("\t" + str(num) + "** 3 = " + str(round(num**3,4)))
print("\t" + str(num) + "** 4 = " + str(round(num**4,4)))
print("\t" + str(num) + "** 5 = " + str(round(num**5,4)))
print("\t" + str(num) + "** 6 = " + str(round(num**6,4)))
print("\t" + str(num) + "** 7 = " + str(round(num**7,4)))
print("\t" + str(num) + "** 8 = " + str(round(num**8,4)))
print("\t" + str(num) + "** 9 = " + str(round(num**9,4)))

print("\n Math is fun isn't it")
