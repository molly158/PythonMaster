class Person:
    pass

class Worker(Person):
    pass

class Student(Person):
    pass

class Teacher(Person):
    pass

class Factory:
    def get_person(self,p_type):
        if p_type == 'w':
            return Worker()
        elif p_type == 's':
            return Student()
        else:
            return Teacher()

"""
worker = Worker()
student = Student()
teacher = Teacher()
"""
factory = Factory()
worker=factory.get_person('w')
student=factory.get_person('s')
teacher=factory.get_person('t')

#工厂模式也是一种创建型设计模式，它将对象的创建逻辑封装到一个工厂类中，使调用方无需关心具体对象事如何创建的
#只需要告诉工厂需要什么对象就可以