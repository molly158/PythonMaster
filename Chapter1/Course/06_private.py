class Phone:
    #公共变量
    serial_number=None
    producer=None

    #私有成员（变量和方法）不能被对象调用，但是可以被类里的其他成员（变量和方法）调用
    #以__开头
    __current_voltage=1 #目前的电压

    def call_by_5g(self):
        if self.__current_voltage >=1:
            self.__keep_single_core()
            print("les appels 5g sont desormais possibles.")
        else:
            print("defaut d appel, batterie faible.")
    #私有方法
    def __keep_single_core(self):
        print("faire fonctionner l unite centrale en mode monocoeur pr economiser de l energie")

phone=Phone()
phone.call_by_5g()
#私有方法,变量不能被对象直接调用，使用
"""
phone.__current_voltage=50
phone.__keep_single_core()
"""
