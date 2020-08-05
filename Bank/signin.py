class test():
    balance = 100
        

    def credit(self):
        amount = float(input("How much would you like to deposit?"))
        
        self.balance += amount
        
        file = open("cus.csv", "a")
        
        file.writelines(f"{self.balance}\n")
        
        print("Your new balance is - ", self.balance)

    def debit(self):
        amount = float(input("How much would you like to withdraw?"))

        if amount < self.balance:
        
            self.balance -= amount
            
            file = open("cus.csv", "a")
            
            file.writelines(f"{self.balance}\n")
            
            print("Your new balance is - ", self.balance)
        
        elif amount > self.balance:
            print("Insufficient Balance")

test().debit()