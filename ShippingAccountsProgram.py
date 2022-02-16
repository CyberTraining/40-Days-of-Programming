#Shipping Accounts Program
#January 18th 2022#Conditionals Challenge 16: Shipping Accounts Program

#Title
print("Welcome to the Shipping Accounts Application")

#List of users
users=['flarrive', 'mcurnow', 'jsmith', 'mcarey', 'jcole']

#Get user info
username = input("What is your username: ")
username=username.lower().strip()

#is username in the user
if username in users: 
  #print the price list
  print("\nHello " + username + " Welcome back to your account.")
  print("Current shipping prices are as follows:")
  print("\nShipping orders 0-100: \t\t\t$5.10 each")
  print("Shipping orders 100-500: \t\t$5.00 each")
  print("Shipping orders 500-1000: \t\t$4.95 each")
  print("Shipping orders over 1000: \t\t\t$4.80 each")

#Determine price based on the amount of items to ship
  quantity = int(input("\nHow many items would you like to ship: "))
  if quantity < 100:
    cost = 5.10
  elif quantity < 500: 
    cost = 5
  elif quantity < 1000: 
    cost = 4.95
  elif quantity >= 1000:
    cost = 4.80
   
   #display total cost 
  total=float(cost)*int(quantity)
  total=round(total,2)
  print("To ship " + str(quantity) + " items the total cost will be $" + str(total) + " at $" + str(cost) + " per item.")
  
  #place order if userwants to

  choice=input("\nWould you like to place the order (y/n) ").lower()
  if choice.startswith("y"):
    print("Okay.  Shipping your " +str(quantity) + " items.")
  else: 
    print("Okay no order will be placed.")  

else:
  print("You're username is not in the list. ")
  print("Exiting..........") 
