class Phone:
    serial_number=None
    producer="Huawei"

    def call_by_5g(self):
        print("Father 5g calls")

class MyPhone(Phone):
    face_id=True
    producer="apple"

    def call_by_5g(self):

        #1.调用父类的属性
        print(f"la marque de la classe pere est :{Phone.producer}")
        #调用父类的行为
        Phone.call_by_5g(self)

        #2.调用父类的属性
        print(f"la marque de la classe pere est :{super().producer}")
        #调用父类的行为
        super().call_by_5g()

my_phone=MyPhone()
print(my_phone.producer)
my_phone.call_by_5g()
