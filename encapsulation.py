# banking system 

class BankAccount:
    account_holder_name="unknown"
    _account_type="Savings"


    def __init__(self,pin):
        self.__balance=0
        self.__pin=pin


    def set_pin(self,new_pin):
        self.__pin=new_pin
        print("Pin has been set.")
   
    def get_pin(self):
        return self.__pin


    def verify_pin(self,new_pin):
        return new_pin==self.__pin


    def get_balance(self,pin):
        if self.verify_pin(pin):
            return self.__balance
        else:
            return "Incorrect pin."
   
    def set_balance(self,pin,amount):
        if self.verify_pin(pin):
            self.__balance+=amount
            print("The updated balance is",self.__balance)
        else:
            print("Enter valid PIN")



BA=BankAccount(7019)
# print("Old account name is",BA.account_holder_name)
BA.account_holder_name="Lakshmi"
print("The updated account holder name is",BA.account_holder_name)
# print("The account old pin is",BA.get_pin())
BA.set_pin(1234)
print("The account new pin is",BA.get_pin())
print("The old balance is",BA.get_balance(1234))
BA.set_balance(1234,100)