# class father:
#     def __init__(self,surname,name):
#         self.surname=surname
#         self.father_name=name
#     def display_surname(self):
#         print("the surname is ",self.surname)
#     def display_father_name(self):
#         print("the surname is ",self.father_name)


# class son(father):
#     def __init__(self,name,surname,father_name):
#         self.name=name
#         super().__init__(surname,father_name)
#     def display_name(self):
#         print("The name of the son is",self.name)


# class daughter(father):
#     def __init__(self,name,surname,father_name):
#         self.name=name
#         super().__init__(surname,father_name)
#     def display_name(self):
#         print("The name of the daughter is ", self.name)


# obj=son("Madan","Gowda","Manju")
# obj.display_name()
# obj.display_father_name()


# obj1=daughter("Lakshmi", "Gowda", "Manju")
# obj1.display_name()
# obj.display_father_name()

class BankAccount:
    def __init__(self, account_holder):
        self.account_holder=account_holder
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount


    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.display_balance()
        else:
            print("You have insufficient amount in your Account.")


    def display_balance(self):
        print("The balance is",self.balance)


class SavingsAccount(BankAccount):
    def __init__(self,interest_rate,name):
        temp_interest=interest_rate/100
        self.interest_rate=temp_interest
        super().__init__(name)
    def add_interest(self):
        self.balance*=(1+self.interest_rate)
        super().display_balance()


class CurrentAccount(BankAccount):
    def __init__(self,overdraft_limit, name):
        self.overdraft_limit=overdraft_limit
        super().__init__(name)
    def withdraw_with_overdraft(self,amount):
        if amount<self.balance+self.overdraft_limit:  # 590 < 600
            self.balance-=amount
            super().display_balance()
        else:
            print("Overdraft limit is exceeded")


SA=SavingsAccount(10,"Raja")
CA=CurrentAccount(100,"Raja")


# SA.deposit(100)
# SA.withdraw(30)
# SA.add_interest()


CA.deposit(500)
CA.withdraw_with_overdraft(590)
