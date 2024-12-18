class Payment:
    def process(self):
        print("processing a pament")

class CardPayment(Payment):
    def process(self):
        return f'{super().process()} \n processing card payment'
    
c = CardPayment()
print(c.process())