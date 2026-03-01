class Phone:
    serial_number = None
    producer = None

    __current_voltage = 0
    __is_5g_enable = None

    def call_by_5g(self):
        if self.__current_voltage >=1:
            self.__is_5g_enable = True
        else:
            self.__is_5g_enable = False
        self.__check_5g()

    def __check_5g(self):
        if self.__is_5g_enable is True:
            print("5g active")
        else:
            print("5g off, utilisation d un reseau 4g")
phone=Phone()
phone.call_by_5g()