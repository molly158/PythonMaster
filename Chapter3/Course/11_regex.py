# 正则表达式（regular expression），简称 regex
# 用一套特殊规则，去描述“什么样的字符串是我想找的”

import re

s1="python alex python alex python alex"

#从字符串开头开始匹配
result=re.match("python",s1)
print(result)
#span() 返回匹配内容的起始和结束位置
print(result.span())
# group() 把真正匹配到的内容取出来
print(result.group())

s2="python alex python alex python alex"
#re.match() 只看开头
result=re.match("python",s2)
print(result)

s3="1pythonalexpythonalexpythonalex"
#re.search（）整个字符串里找第一个
result=re.search("python",s3)
print(result) #<re.Match object; span=(1, 7), match='python'>
print(result.span()) #(1, 7)
print(result.group()) #python

s4="alex666"
#没找到返回none
result=re.search("python",s4)
print(result)

s5="1pythonalexpythonalexpythonalex"
#re.findall() 找出所有
result=re.findall("python",s5)
print(result)

s6="1pythonalexpythonalexpythonalex"
#没找到就返回一个空列表[]
result=re.findall("li",s6)
print(result)