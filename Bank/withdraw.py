balance = float()
def credit():
    global balance
    amount = float(input("How much would you like to deposit?"))
    balance = balance + amount
    print("Your new balance is - ", balance)
credit()