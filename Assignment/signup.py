# sign up

Firstname = input('What is your Firstname?: ')
Lastname = input('What is your Lastname?: ')
username = input('Pick a username:')
Password = input('Type in a password:') 
confirm_password = input('Confirm your password:')

file = open("database.csv", "a")

file.write(f"{Firstname}, {Lastname}, {username}, {Password}\n")
file.close
