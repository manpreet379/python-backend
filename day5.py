class BankAccount:
    total_accounts=0
    
    
    def __init__(self,balance,acc_type,name):
        self.name=name
        self.__balance=balance
        self.acc_type=acc_type
        BankAccount.total_accounts+=1
        
    
    def get_balance(self):
        return self.__balance
    
    def get_acc_details(self):
        return (f"Account holder name: {self.name}, Type:{self.acc_type}, Balance: Rs{self.__balance}")
    
    def deposit(self,amount):
        if(amount<0):
            print("Deposit must be positive")
        else:
            self.__balance+=amount
            print("Money deposited!")
    
    def withdraw(self,amount):
        if(self.__balance>=amount):
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self.__balance}")
        else:
            print("Not enough balance")
            


acc1 = BankAccount( 5000, "Savings","Manpreet")
acc2 = BankAccount (3000, "Checking","Dev Raj")

# Accessing account details
print(acc1.get_acc_details())
print(acc2.get_acc_details())

#deposit
acc1.deposit(1000)

#withdraw
acc2.withdraw(500)

acc2.withdraw(5000)


print(f"Total Bank Accounts: {BankAccount.total_accounts}")


