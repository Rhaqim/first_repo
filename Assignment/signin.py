# sign in

input_username = input('What is your username?')
input_Password = input('What is yourpassword?') 

file = open("database.csv", "r")

for line in file.readlines():
    saved_username, saved_password = line.replace("\n", "").split(",")[2:]
    if saved_username == input_username and saved_password == input_Password:
        print("Welcome, ", {saved_username})
        break
else:
    print("Please Input correct details")


