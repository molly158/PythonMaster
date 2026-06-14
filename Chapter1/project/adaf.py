class Personnage:
    def __init__(self,name,age):
        self.name=name
        self.age=age
asterix=Personnage("asterox",18)
b=asterix
b.age=90
print(asterix.age)

asterix.age=90
print(asterix.age)

