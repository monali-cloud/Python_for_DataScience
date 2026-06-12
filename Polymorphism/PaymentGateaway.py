#Create a parent class Payment with method pay().
#Create child classes:
#UPI
#CreditCard
#NetBanking
#Override pay() in each class.
#Use a loop to process payments

class payment:
    def pay(self):
        print("processing payment")
    
class UPI(payment):
    def pay(self):
        print("payment through UPI")
        
class CreditCard(payment):
    def pay(self):
        print("payment through credit card")
        
class netbanking(payment):
    def pay(self):
        print("payment through netbanking")                
            
payments=[UPI(),CreditCard(),netbanking()]

for p in payments:
    p.pay()        