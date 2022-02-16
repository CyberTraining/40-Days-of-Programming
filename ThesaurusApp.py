#40 days of coding
#Janruay 30th 2022
#Dictionary Challenge 1: Thesaurus App

import random

#title of the application
print("Wlecome to the Thesaurus Application!")

thesaurus={
  'hot':['balmy', 'summery', 'tropical', 'boiling, scorching'],
  'cold':['chilly', 'cool', 'freezing', 'frigid', 'polar'],
  'happy':['content', 'cheery', 'merry', 'jovial', 'jocular'],
  'sad':['unhappy', 'downcast', 'miserable', 'glum', 'melancholy']}


print("Here are the words in the Thesaurus: ")

for key in thesaurus.keys():
  print("\t\t\t-\t" + key)

choice=input("Choose a word from the thesaurus and I will give you a synonym: ")


if choice in thesaurus.keys():
  index = random.randint(0,4)
  print("A synonym for " + str(choice) + " is " +thesaurus[choice][index] +".")

else: 
  print("Sorry that word is not in the thesaurus")
