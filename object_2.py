class Product:
    tax = 1.1

    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
    
    def total(self):
        return int(self.price * self.quantity * Product.tax)
    
xperia = Product(23000, 2)
total = xperia.total()
print("金額は、" + str(total) + "円です")