
import random
import json
from typing import Union

var_1:int=10
var_2:float=3.14

class Student:
    pass
stu:Student=Student()

name:str="Alex"
print(name.count("A"))

my_list2:list[int]=[1,2,3]
my_list3:tuple[int,bool,str]=(1,True,"apple")
my_set:set[int]={1,2,3}
my_dict:dict[str,int]={"age":18}

var4=random.randint(1,10)
data='{"age":18}'
var5=json.loads(data)
var6=Student()

def add(x,y):
    return x+y
result=add(1,2)
print(result)

def func(data:list[int]) -> list[int]:
    data.append(4)
    return data
l=[1,2,3]
func(l)
print(l)

my_list5:list[Union[str,int]]=[1,2,"alex","luna"]
my_dict4:dict[str,Union[int,str]]={"name":"alex","age":18}

def func2(data:Union[int,str]) -> Union[int,str]:
    return data
r=func2([1,2])
print(r)