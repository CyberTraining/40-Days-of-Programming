#January 19th 2022
#Conditionals Challenge 17: Coin Toss Application

import random

#Title
print("Welcome to the Coin Toss Application")

#print the description of the applicatino 
print("I will flip a coin a set number of times")
flip_number=int(input("How many flips would you like in total: "))
visibility=input("Do you want to see each flip output? (y/n): ")

print("\n............Flipping............\n")

#initialize variables
heads = 0
tails = 0

#main loop
for flips in range(flip_number):
  #create the coin object
  coin= random.randint(0,1)

  if coin == 1:
    heads += 1
    if visibility.startswith('y'):
      print("Heads") 
  else:
      tails += 1
      if visibility.startswith('y'):
        print("Tails") 

if heads==tails: 
  print("At " + str(flips + 1) + " flips, the number of heads and tails were equal at " + str(heads)) 

#Calculate the percentage
heads_average=(heads/(heads+tails))*100
tails_average=(tails/(tails+heads))*100
heads_average=round(heads_average,2)
tails_average=round(tails_average,2)

#print the percentage 

print("Results of flipping a coin " +str(flips)+ " times.")
print("Side\t\t  Count \t\t Precentage")
print("Heads\t\t  "+ str(heads)+" \t\t\t " +str(heads_average)+ "%")
print("Tails\t\t  "+ str(tails)+" \t\t\t " + str(tails_average)+ "%")

