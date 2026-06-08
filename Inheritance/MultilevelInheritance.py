#Create:
#Account
#SavingsAccount
#PremiumSavings
#Each class should add one new attribute.
#Display all details from the final child class.

class Account:
    def __init__(self,holder):
        self.holder=holder
        
class savingAcc(Account):
    def __init__(self,holder,balance):
        super().__init__(holder)
        self.balance=balance
        
class premiumSaving(savingAcc):
    def __init__(self,holder,balance,reward_points):
        super().__init__(holder,balance)
        self.reward_points=reward_points
        
    def display(self):
        print("Holder :",self.holder)
        print("Balance :",self.balance)  
        print("Reward pt :",self.reward_points)   
        
d1=premiumSaving("john",50000,250)
d1.display()                          