class employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f"Employee name is {self.name}")

class gamer:
    def __init__(self, game):
        self.game = game
    def show(self):
        print(f"Game name is {self.game}")    

class GE(employee,gamer):
    def __init__(self, name, game):
        self.name=name
        self.game=game

a=GE("Fawad","PUBG")
print(a.name)
print(a.game)
a.show()
print (GE.mro())
#(mro-->Method Resolution Order<--)