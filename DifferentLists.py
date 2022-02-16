#40 days of coding
#November 13th 2021
#List Challenge 7: Different Types of Lists Programs. 

title="Different Types of Lists"
print(title)

#defining my List
numStrings=['15', '100', '55', '42']
numInt=[15, 100, 55, 42]
numFloats=[2.2, 5.0, 1.245, 0.142857]
numList=[[1,2,3], [4,5,6],[7,8,9]]

#summary of each List
print("\t\t Summary Table")

print("\nThe Variable numStrings is a " +str(type(numStrings))+".")
print("It contains the elements: " + str(numStrings))
print("The element " + numStrings[0] + " is a " + str(type(numStrings[0]))+ ".")

print("\nThe Variable numInt is a " +str(type(numInt))+".")
print("It contains the elements: " + str(numInt))
print("The element " + str(numInt[0]) + " is a " + str(type(numInt[0]))+ ".")

print("\nThe Variable numFloats is a " +str(type(numFloats))+".")
print("It contains the elements: " + str(numFloats))
print("The element " + str(numFloats[0]) + " is a " + str(type(numFloats[0]))+ ".")

print("\nThe Variable num_strings is a " +str(type(numList))+".")
print("It contains the elements: " + str(numList))
print("The element " + str(numList[0]) + " is a " + str(type(numList[0]))+ ".")

#sorting the lists
numStrings.sort()
numInt.sort()

print("\n Now sorting numStrings and numInts...")
print("Sorted numStrings: " + str(numStrings))
print("Sorted numStrings: " + str(numInt))
print("\n Strings are sorted alphabetically while integers are sorted numerically!!!")
