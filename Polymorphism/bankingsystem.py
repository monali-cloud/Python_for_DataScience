#Create a parent class Account with:
#withdraw(amount)
#Create child classes:

#SavingsAccount
#CurrentAccount

#Each should implement its own withdrawal rules.

#Example:

#Savings Account: Withdrawn ₹500
#Current Account: Withdrawn ₹500

#Use a list of accounts and call withdraw() polymorphically.

class account:
    def withdraw(self):
       
        print("amount")
        
class savingacc(account):
    def withdraw(self):
        print("withdrawn 500rs ")
        
class currentacc(account):
    def withdraw(self):
          print("withdrawn 500 rs")              
          
a1=account()          
s1=savingacc()
c1=currentacc()

a1.withdraw()
s1.withdraw()
c1.withdraw()
          
