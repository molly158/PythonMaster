import re

s="alex @@python2 !!666 ## python3 "
#把字符串里的所有单个数字找出来 \d
#\d: 匹配一个女数字字符，也就是0到9
#r : raw string , 原始字符串，避免\被python当成转义字符(\n 换行)处理
result1=re.findall(r"\d",s)
print(result1)

#\W（大写)：匹配“非字母，非数字，非下划线"的字符
#\w（小写)：匹配“字母，数字，下划线"的字符
result2=re.findall(r"\W",s)
print(result2)

#把字符串里所有英文字母一个一个找出来
#a-z : 所有小写字母 A-Z : 所有大写字母
result3=re.findall(r"[a-zA-Z]",s)
print(result3)

s1="a804233"
#^:匹配字符串开头
#$:匹配字符串结尾
#{6,10}：匹配前一个规则的字符出现6到10次
#从开头到结尾，只允许数字和英文字母，总长度必须在6到10位之间
result4=re.findall(r"^[0-9a-zA-Z]{6,10}$",s1)
print(result4)

s2="804233992"
#第一位qq号不能是0，后面再跟4到10个数字
result5=re.findall(r"^[1-9][0-9]{4,10}$",s2)
print(result5)

#*：匹配前一个规则的字符出现0至无数次
#+：匹配前一个规则的字符出现1至无数次
# [\w-]+ : 表示字母，数字，下划线，还可以有-，而且至少一个字符
#?: ==> 非捕获组
#(?:\.[\w-]+) => 可以出现也可以不出现 yixue.liang@dauphine.eu avc "."
r3=r'^[\w-]+(?:\.[\w-]+)*@(?:qq|163|gmail)(?:\.[\w-]+)+$'
s3='sgsgkxkx@gmail.com'
result5=re.findall(r3,s3)
print(result5)