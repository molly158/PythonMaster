class Phone:
    serial_number=None
    producer="Huawei"

    def call_by_5g(self):
        print("5g calls")

class NFCReader:
    nfc_type="Fifth generation"
    producer="HM"

    def read_card(self):
        print("Read NFC card")
    def write_card(self):
        print("Write NFC card")

class RemoteControl:
    rc_type="IR Remote control"

    def control(self):
        print("infrared remote control opening")

class MyPhone(Phone,NFCReader,RemoteControl):
    pass

xiaomi_phone=MyPhone()
xiaomi_phone.call_by_5g()
xiaomi_phone.control()

print(xiaomi_phone.producer) #phone在NFC前面
