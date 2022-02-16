#40 days of coding
#November 3rd 2021
#Basic Data Types Challenge 3: Temperature Conversion App. 


title="Welcome to the Temperature Converison Program"
print(title)

#gather user input
temp=float(input("What is the given temperature in degrees Fahrenheit: "))

#Celsius conversion
celsius=float((temp-32)*.5556)

#Kelvin conversion
kelvin=float(celsius+273.15)

#round to four decimal places
roundedCelsius=round(celsius, 4)
roundedKelvin=round(kelvin, 4)

#output message
print("Degrees Fahreneheit:       "+ str(temp))
print("Degrees Celsius:           "+ str(roundedCelsius))
print("Degrees Kelvin:            "+ str(roundedKelvin))
