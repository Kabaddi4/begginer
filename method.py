class Smartphone:
    def __init__(self, name):
        self.name = name
    
    def buy(self, place):
        print(self.name + "を" + place + "で購入した")
    
print("=スマホを購入する=")
iphone = Smartphone("iphone")
#iphone.buy("店頭")

xperia = Smartphone("xperia")

smartphone = [iphone, xperia]   #リスト化
for devise in smartphone:   #変数を作成し、リストの値を代入
    devise.buy("店頭")  