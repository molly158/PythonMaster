class Phone:
    serial_number = None
    producer= None
    def call_by_4g(self):
        print("4g calls")

#1. 继承： class 类（副类）：
#           新类的属性和方法
#继承会把副类的成员变量和方法都拿过来，都可以直接用
class Phone2026(Phone):
    face_id=True

    def call_by_5g(self):
        print("2026 latest 5g calls")

phone2026=Phone2026()
phone2026.producer="Apple"
phone2026.call_by_4g()
phone2026.call_by_5g()

