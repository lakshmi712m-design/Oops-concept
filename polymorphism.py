class Payment:
    def pay(self):
        print("Payment successfully done")
class Googlepay(Payment):
    def pay(self):
        print("payment is done thruogh Googlepay")
class PhonePe(Payment):
    def pay(self):
        print("payment is done thruogh Phonepe")
class creditcard(Payment):
    def pay(self):
        print("payment is done thruogh credit card")

gpay=Googlepay()
gpay.pay()
phonepe=PhonePe()
phonepe.pay()
cd=creditcard()
cd.pay()
