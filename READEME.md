# Python master
## Chapter 1 面向对象
### 1. 类和方法
* 类里有两个部分
  * 属性（成员变量）
  * 行为（成员方法）

* 注：函数在类里叫方法（特征：self）

* 类是程序中的“蓝图”，必须基于它们生成实体（对象）才能正常运行。

* 这种方法被叫做面向对象编程（object oriented programmation)

  ```python
  #创建一个类
  #class 类名：
  #   属性
  #   行为
  
  class Student:
      #属性（成员变量）：名字
      name=None
  
      #行为：成员方法
  
  #创建对象
  stu_1=Student()
  stu_2=Student()
  stu_1.name="Leo"
  stu_2.name="Laurent"
  print(stu_1.name)
  ```

### 2. Self
* self:代表对象本身

* self会出现在形式参数列表中，但是不占位（会被忽略）

  ```python
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
  student.say_hi() # bonjour a ts j m appelle {student.name} et j ai {student.age} ans.
  #==> bonjour a ts j m appelle alex et j ai 18 ans.
  student.say_hi2("yes")
  ```

### 3. 构造方法
* \_init_ 

* 当创建对象的时候会自动执行

* 创建对象的时候传参数，会自动传递到\_init_构造方法

  ```python
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
  ```

### 4. 魔法方法

```
_init_ 构造方法 用于创建类对象的时候设置初始化行为
_str_ 用于实现类对象转字符的行为
_lt_ 用于两个类对象进行小于或大于比较
_le_用于两个类对象进行小于等于或大于等于比较
_eq_ 两个类进行相等比较
```

### 5. 三大特征

#### 5.1 封装

* 在类中对现实世界的元素(属性与方法)进行描述，这一概念被称为封装
* 私有成员变量，私有成员方法
  * 以__开头的变量或方法
  * 对象不能访问私有成员(变量与方法)
  * 但是类里的其他成员可以访问同类的私有成员

* ```python
  class Phone:
      #公共变量
      serial_number=None
      producer=None
  
      #私有成员（变量和方法）不能被对象调用，但是可以被类里的其他成员（变量和方法）调用
      #以__开头
      __current_voltage=1 #目前的电压
  
      def call_by_5g(self):
          if self.__current_voltage >=1:
              self.__keep_single_core()
              print("les appels 5g sont desormais possibles.")
          else:
              print("defaut d appel, batterie faible.")
      #私有方法
      def __keep_single_core(self):
          print("faire fonctionner l unite centrale en mode monocoeur pr economiser de l energie")
  
  phone=Phone()
  phone.call_by_5g()
  #私有方法,变量不能被对象直接调用，使用
  """
  phone.__current_voltage=50
  phone.__keep_single_core()
  """
  ```

#### 5.2 继承

* 继承是指一个类继承了另一个类的成员方法和变量

* 单继承

  ```python
  class Phone:
      serial_number = None
      producer= None
      def call_by_4g(self):
          print("4g calls")
  
  #1. 继承： class 类（副类）：
  #           新类的属性和方法
  #继承会把副类的成员变量和方法都拿过来，都可以直接用
  class Phone2026(Phone): #class 类名（父类1，2，...）
      face_id=True
  
      def call_by_5g(self):
          print("2026 latest 5g calls")
  
  phone2026=Phone2026()
  phone2026.producer="Apple"
  phone2026.call_by_4g()
  phone2026.call_by_5g()
  ```

* 多继承

  ```python
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
  ```

* 重写(override)

  * 重写父类的属性或成员方法

```python
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
```

#### 5.3 多态

* 多态意味着 使用不同的对象实现不同的行为 可以得到不同的状态

* 比如：定义一个函数(方法)， 通过类型注解声明它需要父类的对象，但在实际调用时传入子类的对象来执行操作，从而得到不同的运行状态

* 抽象类：只有抽象方法

* 抽象方法：一个方法空实现(只有pass)

  ```python
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
  ```

MySQL is configured to only allow connections from localhost by default

To connect run:

​    mysql -u root -p

To start mysql now and restart at login:

  brew services start mysql

show databases; (展示数据库)



## Chapter 2 SQL

## Chapter 3 Python 高级

## Chapter 4 Git

### 1.版本控制器

+ 集中式(SVN): 版本库集中存放在中央服务器上。必须联网才能工作。
+  分布式(Git)：每个人的电脑上都是一个完整的版本库，包含全部历史。工作时不需要联网。

### 2. Git的历史

+ Git 是一个开源的分布式版本控制系统，由Linus Torvalds为管理Linus内核开发而创建的。

### 3.Git工作流程

+ 工作区：worksplace 修改代码的d地方
+ 暂存区：Index/Stage, 在 `.git`目录中，准备提交的修改清单(`… 再加一个，`)
+ 本地仓库：Repository 在`.git`目录中，所有已经提交版本的历史
+ 远程仓库：Remote 在服务器上(Github，Gitee)，与团队共享的交换点

七个命令：

+ `clone`: 从远程仓库中克隆代码到本地仓库

+ `chekout`: 从本地仓库检出一个分支到工作区进行修订 (切换分支)

+ `add`： 提交前先把修改放进暂存区

+ `commit `：把暂存区提交到本地仓库。本地仓库保存每一个历史版本

+ `fetch`：把远程仓库的更新抓取到本地仓库，不做任何合并，平时用得较少

+ `pull`: 从远程仓库拉到本地并自动合并到当前分支。`pull`=`fetch`+`merge`

+ `push`: 修改完成 需要和团队共享时，把代码推送到远程仓库

  

### 4.基础命令

+ `git init`: 获取本地仓库

+ `touch filename.format `: commande ds le Terminal permet de creer un ficher

+ `git add 文件名`: 把文件的修改加入暂存区

+ `git add .`： 把所有修改加入暂存区

+ ` git commit -m "注释内容"`: 把暂存区提交到本地仓库的当前分支

+ `git log`： 查看提交记录

+ ` git reset —hard commitID`: 版本回退(切换到指定版本)

  ``` python
  (base) yixueliang@YixuesMacBookAir test % git log
  commit 4a3131aa6f74c837f3edaf0e31ff2fd1fe06d713 (HEAD -> main)
  Author: yixueliang <yixueliang0302@gmail.com>
  Date:   Sun Oct 11 10:42:59 2026 +0200
  
      update file01
  
  commit 23ea68024365adf8c13c01dfaf9fc4685265ee67
  Author: yixueliang <yixueliang0302@gmail.com>
  Date:   Sun Oct 11 10:39:11 2026 +0200
  
      commit 001
      
  (base) yixueliang@YixuesMacBookAir test % git reset --hard 23ea68024365adf8c13c01dfaf9fc4685265ee67
  
  HEAD is now at 23ea680 commit 001
  ```

+ `git reflog`: 查看已被删除的提交记录

  ``` python
  (base) yixueliang@YixuesMacBookAir test % git reflog
  23ea680 (HEAD -> main) HEAD@{0}: reset: moving to 23ea68024365adf8c13c01dfaf9fc4685265ee67
  4a3131a HEAD@{1}: commit: update file01
  23ea680 (HEAD -> main) HEAD@{2}: commit (initial): commit 001
  ```

+ ` git status`: 查看修改的状态(暂存区 工作区)

  ``` python
  (base) yixueliang@YixuesMacBookAir test % git status
  On branch main
  nothing to commit, working tree clean
  ```

+ `git branch`: 查看分支

+ `git checkout namebranch`: 切换到namebranch分支











