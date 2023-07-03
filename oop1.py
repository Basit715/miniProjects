class BankAccount:
    def __init__(self,account_holder,  account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def display(self):
        print(f"Bank account holder {self.account_holder}")
        print(f"account number {self.account_number}")


    def deposit(self, amount, sender_account):
        self.balance += amount
        print(f"Your account has been credited with Rs{amount} inr from {sender_account}")

    def withdraw(self, withdrawal_amount):
        if self.balance < withdrawal_amount:
            print("Insufficient balance")
        else:
            self.balance -= withdrawal_amount
            print(f"Your account has been debited with Rs{withdrawal_amount}, account balance {self.balance}")

    def checkBal(self):
        print(f"Balance: {self.balance}")

while True:
    inp = int(input("Enter 0 for creating bank account,  1 for withdrawal, 2 for deposit, 3 for display,4 for check balance and 9 for exit: "))

    if inp == 0:
        username = input("Enter your username: ")
        account_holder_name = input("Enter the account holder name: ")
        account_number = input("Enter the account number you have been assigned with: ")

        username = BankAccount(account_holder_name, account_number)
        print(f"Successfully added your account")
    elif inp == 1:
        amt = int(input("Enter the amount you need to withdraw: "))
        username.withdraw(amt)
    elif inp == 2:
        amt = int(input("Enter the amount you have to deposit: "))
        sender_account = input("Senders account number: ")
        username.deposit(amt, sender_account)
    elif inp == 3:
        username.display()
    elif inp == 4:
        username.checkBal()

    elif inp == 9:
        exit()




















