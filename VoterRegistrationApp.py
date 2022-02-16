#40 days of coding
#January 21 2022
#Conditional Challenge 18: Voter Registration App. 

#title
print("Wlecome to the Voter Registration App")

#ask user for the name
name=input("Please Enter your Name: ")
name=name.title()

#Enter age
age=int(input("Please enter your Age: "))

#list the parties
parties=["Republican", "Democratic", "Independent", "Libertarian", "Green" ]
# are the old enough to vote?
if age > 17: 
  print("Congratulations " +str(name)+ "!  You are old enouigh to register to vote.")
  print("\n Here is a list of political parties to join: ")
  
  for party in parties:
    print("\t\t\t-\t" + party)

#Get users party choice
  party_choice=input("\n Which party would you like to join: ")
  party_choice=party_choice.title().strip()
  
  if party_choice in (parties):
    print("Congratulations " +(name)+ "!  You have joined the "+(party_choice)+"!")




else:
  print("You are not old enough to vote.")
  print("Good Bye...")
