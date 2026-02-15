class Student:
    #成员变量
    name=None
    age=None
    tel=None

    def __init__(self,name,age,tel):
        self.name=name
        self.age=age
        self.tel=tel
        print(" la classe etudiant cree un objet")
stu=Student("Alex","18","110")
print(stu.name)

"""""
#创建对象
stu_1=Student()
stu_1.name="Alex"
stu_1.age=18
stu_1.tel=110

stu_2=Student()
stu_1.name="Luna"
stu_2.age=19
stu_1.tel=120
"""


