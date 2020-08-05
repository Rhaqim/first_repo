balance = 100
def debit():
    global balance
    amount = float(input("How much would you like to withdraw?"))
    if amount < balance:
        balance -= amount
        print("Amount withdrawn is - ", amount, "New balance is - ", balance)
    elif amount > balance:
        print("Insufficient Balance")
debit()