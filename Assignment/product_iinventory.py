import datetime

Product_name = input('What is the name of your product? ')
Product_des = input('Describe your product: ')
Product_size = int(input('How many products are you selling? '))
today = datetime.datetime.now()
date = f"{today.day}-{today.month}-{today.year}"
logged_in_username = "username"

file = open("products.csv", "a")

file.write(f"{Product_name},{Product_des},{Product_size},{date}\n")
file.close


