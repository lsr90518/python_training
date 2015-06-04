import random

class Player(object):
    def __init__(self):
        self.name = "NONAME"
        self.attack = 0

    def get_damage(self, defense):
        base = self.attack // 2 - defense // 2
        damage = base * random.randint(85, 100) //100
        return damage if damage > 1 else 1

class Administrator(object):
    def ban(p):
        print(p.name + "do Ben")


class GameMaster(Administrator, Player):
    def __init__(self):
        super(GameMaster,self).__init__()
    def warp(self, target):
        print(target + "niwa-pu")

    def get_damage(self, defense):
        return 999


if __name__=="__main__":
    p = Player()
    p.attack = 120
    print(p.name, p.get_damage(26))

    gm = GameMaster()
    gm.attack = 160
    print(gm.name, gm.get_damage(26))
    gm.warp("ariahen")

    print(GameMaster.mro())
