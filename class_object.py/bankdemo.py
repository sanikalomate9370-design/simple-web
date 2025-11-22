#write python code to create calss bankdemo having attribute
#bank_accout_number,name,balance
#and methods deposite,withdraw, checkbalance of account
class bankdemo:
    def __init__(self,bank_acc,name,balance):
        self.bank_acc
        self.name
        self.balance
    def deposite(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        self.balance -+ amount
    def balance_check(self):
        print("current balance is:",self.balance)
b1= bankdemo (2004,"sanika lomate",10000)
b1.deposite(5000)
b1.balance_check()
b1.withdraw(3000)
b1.balance_check()
     
    