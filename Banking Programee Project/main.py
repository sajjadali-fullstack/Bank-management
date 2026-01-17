
# BANKING APPLICATION
'''
accounts.py                      transactions.py                    reports.py
-----------                      ---------------                    ------------
def createAccount():             def deposit():                     def printPassbook():
def updateAccount():             def withdraw():                    def printStatement():
def deletingAccount():           def findBalance():
                                 def reqCheBook():
'''
'''
class --> Blue print 
Object --> actual account
'''

#                                           Create Account Programme:

class Account:
    def __init__(self, a, b, c):
        self.account_no = a
        self.balance = b
        self.cname = c

    # 1. Deposit
    def deposit(self, t):
        self.balance = self.balance + t

    # 2. Withdraw
    def withdraw(self, t):
        if self.balance < t:  # True statement
            print("Insufficient Funds!")
        else:  # False Statement
            self.balance = self.balance - t

    # GetBalance
    def getBalance(self):
        return self.balance

    def printAccount(self):
        print(f'Account NO : {self.account_no}, \nCustomer Name : {self.cname}, \nBalance : {self.balance}')


acc = None

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Balance")
    print("5. Check Balance")
    print("6. Account Info")
    print("7. Exit")

    # Giving Options
    print('--------------------😉')
    options = int(input("Enter Your Choice? : "))
    print('-------------------->')
    print()

    # 1. Create Account
    if options == 1:

        a = int(input("Account No : "))
        c = input("Customer Name ? : ")
        b = int(input("Opening Balance? : "))
        acc = Account(a, b, c)

        print('💕---------------------------------💕')
        print("    ACCOUNT CREATED SUCCESSFULLY! ☑️")
        print('🤩---------------------------------🤩')

    # 2. Deposit
    elif options == 2:
        if acc is None:
            print("Please First Create an Account!")
            print('❌-------------------------------❌\n')
        else:
            amt = int(input("Amount? : "))
            acc.deposit(amt)
            print("Deposit Successfully...!💵\n")

    # 3. Withdraw
    elif options == 3:
        if acc is None:
            print("Please Create an account First!")
            print('❌-------------------------------❌\n')
        else:
            amt = int(input("Amount to Withdraw? : "))
            acc.withdraw(amt)
            print("Thank you !")

    # 4. Balance
    elif options == 4:
        if acc is None:
            print("Please Create an account First!")
            print('❌-------------------------------❌\n')
        else:
            bal = acc.getBalance()
            print(f'Balance is : {bal:.2f}\n')

    # 5. Check Balance
    elif options == 5:
        if acc is None:
            print("Please Create an account First!")
            print('❌-------------------------------❌\n')
        else:
            acc.printAccount()
            print(f'Total Balance : {c}')

    # 6. Account Info
    elif options == 6:
        if acc is None:
            print("Please Create an account First!")
            print('❌-------------------------------❌\n')
        else:
            acc.printAccount()

    # 7. exit()
    elif options == 7:
        print("Thank You Visit Again")
        break
    else:
        print('Some went wrong try again!')


