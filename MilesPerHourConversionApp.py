#40 days of coding
#November 2nd 2021
#Challenge Problem 2: Miles per Hour Conversion App. 

title="Welcome to the MPH to MPS Converison App"
print(title)

#gather the users input
speed=input("What is your speed in miles per hour: ",)
#convert to mps
convertedSpeed=float(speed)*0.4474

roundedSpeed=round(convertedSpeed, 2)


print("Your speed in meters per second is: " + str(roundedSpeed)+ ".")
