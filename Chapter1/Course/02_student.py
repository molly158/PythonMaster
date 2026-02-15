class Student:
    #成员变量
    name=None
    age=None

    #成员方法（函数在类里是一个方法
    def say_hi(self): #self:区别stu1 et stu2
        print(f"bonjour je m appelle {self.name} et j ai {self.age} ans.")
#创建对象
stu_1=Student()
stu_1.name="Alex"
stu_1.age=18
stu_1.say_hi()



