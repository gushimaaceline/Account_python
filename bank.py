
from datetime import datetime, time


class Account:
    def __init__(self,name,phone):
            
            self.transactions=[]
            self.name=name
            self.phone=phone
            self.transaction_fee=500
            self.balance=0
            self.loan=0
            self.loan_limit=500000
    def deposit(self,amount):
        try:
            amount+10
        except TypeError:
            return f"Please enter amount in figures"
            amount
        if amount<=0:
            return f"Please deposit a valid amount"

        else:
             self.balance+=amount
             transaction={
             "amount":amount,
             "balance":self.balance,
             "time":datetime.now(),
             "narration":"Deposit"
                }
             self.transactions.append(transaction)
             return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"
    def get_statement(self):
        for transaction in self.transactions:
            narration=transaction["narration"]
            amount=transaction["amount"]
            balance=transaction["balance"]
            time=transaction["time"]
            date=time.strftime("%D" )
            print (f"{date}.. {narration}..{amount}..Balance {balance}")
    def withdraw(self,amount):
        try:
            amount+10
        except TypeError:
            return f"Please deposit a valid amount"

        total_amount=amount+self.transaction_fee
        if amount<=0:
            return "You can't withdraw negative amount "
        elif self.balance<total_amount:
            return "You can have insufficient balance"
        else:
            self.balance-=total_amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "time":datetime.now(),
                "narration":"withdraw"
                }
                
            self.transactions.append(transaction)
            return f"You have successfully withdrawn {amount} your balance is {self.balance}"
             
    def borrow(self,amount):
        try:
            amount+10
        except TypeError:
            return f"Please enter amount in figures"
       
        if amount>=self.loan_limit:
            return f"You can't borrow"
        elif amount<0:
            return "You can't borrow"
        elif self.loan>0:
            return f"You already have an existing loan"

        else:
            loan_fee=amount*0.05
            self.loan=amount+loan_fee
            self.balance+=amount
            self.loan+=1
            self.balance+=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "time":datetime.now(),
                "narration":"Loan"
                }
            self.transactions.append(transaction)
            return f"hello {self.name}.You have taken a loan of {amount},your new balance is {self.balance} and your loan balance is {self.loan}"


    def repay_loan(self,amount):
        
        
        if amount<=0:
            return "Please deposit a positive amount"
        
        elif amount<self.loan:
            outstanging_loan= self.loan-amount
            return f"You have paid {amount} on your loan and your outstand loan is {outstanging_loan}"
        
        else:
            difference=amount-self.loan
            self.balance+=difference
            self.loan=0
            transaction={
                "amount":amount,
                "balance":self.balance,
                "time":datetime.now(),
                "narration":"Loan"
                }
            self.transactions.append(transaction)
            return f"You have fully paid your loan and your balance is {self.balance}" 
    def transfer(self,amount,account):
        try:
              10+amount
        except TypeError:
                 return f"The amount must be in figures"
        fee=amount*0.05
        total=amount+fee
      
        if total>self.balance:
            return f"your balance is {self.balance} and you need {total} inoder to transfer"
        else:
            self.balance-= total
            account.deposit(amount)
            return f"you have sent {amount} to {account.name} and your balance is {self.balance}" 

class MobileMoneyAccount(Account):
    def __init__(self,name,phone,service_provider):
        Account.__init__(self,name,phone)
        self.serviceProvider=service_provider
        
    def buy_airtime(self,amount):
        try:
              amount+10
        except TypeError:
                 return f"The amount must be in figures"
        if amount<0:
            return f"Enter a positive amount"
        elif amount>self.balance:
            return f"You have insufficient balance"
        else:
            self.balance-=amount
            transaction={
                "amount":amount,
                "balance":self.balance,
                "time":datetime.now(),
                "narration":"You bought airtime"
                }
            self.transactions.append(transaction)
            return f"You have bought airtime of {amount}. Your new balance is {self.balance}"

             
