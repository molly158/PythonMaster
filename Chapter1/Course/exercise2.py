class Student:
    name=None
    age=None
    address=None

    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address
        print(f"[Nom:{self.name}, Age:{str(self.age)}, Address:{self.address}] ")

for i in range(1,6):
    name=input("saisir le nom de l eleve:")
    age=int(input("saisir l age de l eleve:"))
    address=input("saisir l adresse de l eleve:")
    print(f"la saisie des informations sur l etudiant {i} est complete avc les info suivantes :" )
    stu = Student(name, age, address)
    print(f"actuellement en train de saisir le {i}eme eleve, 5 eleves au total doivent etre saisis. ")