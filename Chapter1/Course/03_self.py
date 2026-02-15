class Student:
    name=None
    age=None
    def say_hi(self):
        print(f"bonjour a ts j m appelle {self.name} et j ai {self.age} ans. ")

    def say_hi2(self,msg):
            print(f"bonjour a ts, {msg}")

student=Student()
student.name="alex"
student.age=18
student.say_hi()
student.say_hi2("yes")

