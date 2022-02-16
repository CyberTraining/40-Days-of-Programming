#40 days of coding
#November 13th 2021
#List Challenge 11: Binary Hexadecimal Conversion App. 

import datetime

# Get the time
time=datetime.datetime.now()
year=str(time.year)
month=str(time.month)
day=str(time.day)
hour=str(time.hour)
minute=str(time.minute)

#print the date
print("The current Date and Time: " + year + "/" + month + "/" + day + "\t" + hour + ":" + minute)

#title
title=("\nWelcome to the Binary Hexadecimal Conversion  App.")
print(title)

# Get the user input and generate Lists
max_value = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
decimal = list(range(1, max_value+1))
binary=[]
hexadecimal=[]


for num in decimal:
  binary.append(bin(num))
  hexadecimal.append(hex(num))
print("Generating list.... Complete!")

#get slicing index from user
print("\nUsing slices we will now show a portion of each list")
lower_range=int(input("What decimal number would you like to start at: "))
upper_range=int(input("What decimal number would you like to finish at: "))


#slice through each list individually
print("\nDecimal values from "+ str(lower_range) +" to "+ str(upper_range) + ":")
for num in decimal[lower_range-1:upper_range]:
  print(num)

print("\nBinary values from "+ str(lower_range) +" to "+ str(upper_range) + ":")
for num in binary[lower_range-1:upper_range]:
  print(num)

print("\nHexadecimal values from "+ str(lower_range) +" to "+ str(upper_range) + ":")
for num in hexadecimal[lower_range-1:upper_range]:
  print(num)

#output the whole list to the screen
input("\nPress Enter to see all values from 1 to " + str(max_value) + ".")
print("Decimal----Binary----Hexadecimal")
print("----------------------------------")
for d,b,h in zip(decimal, binary, hexadecimal):
  print(str(d)+"----" + str(b) + "----" + str(h))
