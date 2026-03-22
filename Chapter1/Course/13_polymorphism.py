#polymorphism 必须基于inheritance
#父类只定义方法 在方法里面做空实现
#再由子类去做实现
#这个类就叫抽象类 里面的方法叫抽象方法

class Animal:
    #在父类只定义一个方法 不实现
    def speak(self):
        pass

class Dog(Animal):
    #具体实现交给子类去重写
    def speak(self):
        print("woof woof woof")

class Cat(Animal):
    def speak(self):
        print("meow meow meow")

def make_noise(animal:Animal):
    animal.speak()

dog = Dog()
make_noise(dog)

cat = Cat()
make_noise(cat)


