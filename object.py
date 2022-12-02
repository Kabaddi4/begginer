class Product:
    def __init__(self, smartphone):
            self.smartphone = smartphone
    
    def buy(self):
        print(self.smartphone + "を購入")

action = Product("Xperia")
action.buy()