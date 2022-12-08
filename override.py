class Phone:
    def __init__(self, model):
        self.model = model
    
    def buy(self):
        print(self.model + "を購入した")

class CellPhone(Phone):     #継承
    def evol(self):
        print("携帯電話に進化した")

    def buy(self):
        print(self.model + "をネットで購入した")    #オーバーライド
    
phone = Phone("電話")   #親クラスのインスタンス
phone.buy()

cellphone = CellPhone("携帯電話")      #子クラスのインスタンス
cellphone.evol()
cellphone.buy()