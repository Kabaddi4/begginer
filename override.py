class Phone:
    def __init__(self, model):
        self.model = model
    
    def buy(self):
        print(self.model + "を購入した")

class CellPhone(Phone):
    def evol(self):
        print("携帯電話に進化した")
    
phone = Phone("電話")
phone.buy()

cellphone = CellPhone("携帯電話")
cellphone.evol()
cellphone.buy()