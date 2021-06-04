class Account:
    def __init__(self,name,phone):
            self.name=name
            self.phone=phone
            self.transaction_fee=500
            self.balance=0
            self.loan=0
            self.loan_limit=500000
    def deposit(self,amount):
        if amount<=0:
            return "Please deposit a valid amount"

        else:
             self.balance+=amount
             return f"Hello {self.name} you have deposited {amount} your new balance is {self.balance}"

    def withdraw(self,amount):
        total_amount=amount+self.transaction_fee
        if amount<=0:
            return "You can't withdraw negative amount "
        elif self.balance<total_amount:
            return "You can have insufficient balance"
        else:
             self.balance-=total_amount
             return f"You have successfully withdrawn {amount} your balance is {self.balance}"
             
    def borrow(self,amount):
       
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
            return f"hello {self.name}.You have taken a loan of {amount},your new balance is {self.balance} and your loan balance is {self.loan}"
             
