class Phone:
    serial_number=None
    producer="Huawei"

    def call_by_5g(self):
        print("5g calls")

class MyPhone(Phone):
    face_id=True
    producer="apple"

    #override : 重写父类的属性和行为
    def call_by_5g(self):
        print("child 5g calls")

my_phone=MyPhone()
print(my_phone.producer)
my_phone.call_by_5g()
