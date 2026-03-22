#air conditioner
class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_l_r(self):
        pass

class Midea_MC(AC):
    def cool_wind(self):
        print("climatisation et refroidissement par Midea")
    def hot_wind(self):
        print("chauffage  par Midea")
    def swing_l_r(self):
        print("les climatiseurs Midea se balancent de gauche a droites")


class Gree_MC(AC):
    def cool_wind(self):
        print("climatisation et refroidissement par gree")

    def hot_wind(self):
        print("chauffage  par gree")

    def swing_l_r(self):
        print("les climatiseurs gree se balancent de gauche a droites")

def make_cool(ac:AC):
    ac.cool_wind()

midea_ac = Midea_MC()
gree_ac=Gree_MC()

make_cool(midea_ac)
make_cool(gree_ac)

#抽象类：抽象类不能实例化，只能继承 ； 只有抽象方法
#抽象方法：没有做实现
