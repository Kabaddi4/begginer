class Knob:
    def __init__(self, knob):
        self.knob = knob
    
    def buy(self, price):
        print(self.knob + "は" + str(price) + "円")     #渡す値を文字列にするのでなく、メソッド側でstring型を指定した方が楽かも

squid = Knob("イカ")
squid.buy(299)
