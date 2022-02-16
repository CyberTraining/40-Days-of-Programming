#40 days of coding
#November 3rd 2021
#Basic Data Types Challenge 4: Right Triangle Solver App. 
import math


title="Wlecome to the Right Triangle Solver App"
print("title")

#get the users input
firstLeg=float(input("What is the first leg of the triangle: "))
secondLeg=float(input("What is the second leg of the triangle: "))

#Equations
hypo=math.sqrt((firstLeg **2)+(secondLeg **2))
sp=(firstLeg + secondLeg+ hypo)/2
area=0.5*firstLeg*secondLeg

#Rounding
hypo=round(hypo,3)
area=round(area,3)

# the output
print("For a triangle with legs of " +str(firstLeg)+" and " +str(secondLeg)+ " the hypotenuse is " + str(hypo) +".")

print("For a triangle with legs of " +str(firstLeg)+" and " +str(secondLeg)+ " the hypotenuse is " + str(area) +".")
