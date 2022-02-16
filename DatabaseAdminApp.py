#40 days of coding
#February 4th 2022
#Dictionary Challenge 1: Database Admin Program



#title of the application
print("Welcome to the Database Administration Program!")

#Create a dictionary to hold all username: passworde key-value pairs

logon_information = {
  'admin1' : 'password1',
  'admin2' : 'password2',
  'admin3' : 'password3',
  'admin4' : 'password4', 
  'admin00': 'password00',
  }

#Get the user's username
username=input("Enter your username: ")

#Simulating the Login
# Get the users password
if username in logon_information.keys(): 
  password=input("Enter your password: ")
  if password == logon_information[username]:
    print("\nHello " +username+ "! You are logged in!")
    if username=='admin00':
      print("\nHere is the current user database: ")
      for key, value in logon_information.items():
        print("Username: " + key + "\t\tPassword: " + value)
    else:
      #allow standard user to change their password
      password_change= input("Would you like to change your password (yes/no): ").lower().strip()
      if password_change.startswith('y'):
        new_password = input("Enter new password (min 8 char): ")
        if len(new_password) >= 8:
          logon_information[username] = new_password
        else: 
          print(new_password + "is not the minimum length")
        print("\n"+ username + "Your password is " + logon_information[password] +".")
