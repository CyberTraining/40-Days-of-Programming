#40 days of coding
#November 1st 2021
#Basic Data Types Challenge 1: Letter Counter App. 


name=input("What is your name ", )

print("Hello " + name)
print("I will count the number of times that a specific letter occurs in a message.")

message=input("Please enter a message: ", )
letter=input("Please enter your letter: ",)
message=message.lower()
characterCount=message.count(letter)

print("The letter "+letter+" occures "+str(characterCount)+"times.")
