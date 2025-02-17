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


# class BankAccount:
#     # Class variable to track the total number of accounts
#     total_accounts = 0

#     def __init__(self, holder_name, balance, account_type):
#         self.holder_name = holder_name  # Public instance variable
#         self.__balance = balance  # Private instance variable
#         self.account_type = account_type  # Public instance variable
#         BankAccount.total_accounts += 1  # Increment total accounts

#     # Getter for balance
#     @property
#     def balance(self):
#         return self.__balance

#     # Setter for balance (validates deposit)
#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             raise ValueError("Balance cannot be negative!")
#         self.__balance = amount

#     # Method to deposit money (uses setter)
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount  # Using setter
#             print(f"Deposited ${amount}. New Balance: ${self.balance}")
#         else:
#             print("Deposit amount must be positive!")

#     # Method to withdraw money (validates withdrawal)
#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount  # Using setter
#             print(f"Withdrew ${amount}. Remaining Balance: ${self.balance}")
#         else:
#             print("Invalid withdrawal amount!")

#     # Getter for account details
#     @property
#     def account_details(self):
#         return f"Account Holder: {self.holder_name}, Type: {self.account_type}, Balance: ${self.balance}"

# # Creating account objects
# acc1 = BankAccount("Alice", 5000, "Savings")
# acc2 = BankAccount("Bob", 3000, "Checking")

# # Accessing account details using @property
# print(acc1.account_details)
# print(acc2.account_details)

# # Depositing money
# acc1.deposit(1000)

# # Withdrawing money
# acc2.withdraw(500)

# # Trying to withdraw more than balance
# acc2.withdraw(5000)

# # Checking total accounts created
# print(f"Total Bank Accounts: {BankAccount.total_accounts}")

# # Setting a new balance (using setter)
# acc1.balance = 7000
# print(f"Updated Balance for Alice: ${acc1.balance}")

# # Trying to set a negative balance (raises error)
# # acc1.balance = -500  # Uncomment to see error
def hollow_hourglass(n):
    for i in range(n):
        for j in range((2 * n) - 1):
            if i == 0 or j == i or j == (2 * n) - 2 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    for i in range(n-2, -1, -1):
        for j in range(2 * n - 1):
            if i == 0 or j == i or j == 2 * n - 2 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Set the size of the hourglass
n = 5
hollow_hourglass(n)