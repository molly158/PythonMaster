class Student:
    name=None
    age=None

    def __init__(self, name, age):
        self.name=name
        self.age=age

    #修改对象创建后的打印
    def __str__(self):
        return f'name={self.name}, age={self.age}'
    #<:lt, >:gt
    def __lt__(self, other):
        return self.age < other.age
    #<=:le, >=:ge
    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name


student1=Student("Alex",20)
student2=Student("Luna",20)
print(student1  < student2)
print(student1 == student2)


