name = input("What is your name? ")
email = input("What is your uemail address? ")
password = input("Type in a password ")

file = open("cust_detail.csv", "a")

file.write (f"{name};{email};{password}\n")
file.close
