class Product:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    
    def tax(self):
        return self.price * self.quantity
    
xperia = Product(23000, 2)
print("金額は、" + str(xperia.tax()) + "円です")