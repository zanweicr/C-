# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/01/09 12:52
# @Author  : makabaka
# @Version : python3.9
# @File    : str 


# str1 = 'Then I have a passion for the beauty of handwriting'
"""
字符串的查找
find(子串，开始下标位置，结束下标位置)
index()
count()
rfind()   从字符串的右边开始查找
rindex()  从字符串的右边开始查找
"""

# str1 = 'Then I have and passion and the and of handwriting'

# 1.find()函数 找到返回对应的开始下标，找不到返回-1
# print(str1.find('I'))
# print(str1.find('a', 10, 20))
# print(str1.find('love'))

# 2.index()函数 找到返回对应值 找不到报错
# print(str1.index('I'))
# print(str1.index('a', 10, 20))
# print(str1.index('love'))    #   直接报错 substring not found

# 3.count()函数 查找一个字符在这其中出现的次数 如果没有返回0
# print(str1.count('and'))
# print(str1.count('and', 25, ))
# print(str1.count('love'))

# 4.rfind()函数 跟find类似 不过是从右侧开始  找到的下标还是从左侧开始数

# 4.rindex()函数  跟index类似 不过是从右侧开始  找到的下标还是从左侧开始数


"""
    字符串的修改
    replace()函数 替换 （旧子串，新子串，替换次数）
    split()函数 分割    (分割字符，num)  分割之后返回一个列表 num+1个元素 而且分割字符丢失
    join()函数 合并     将一个列表合并为字符串 
"""
# join()函数 详细说明一下
# list1 = ['aa', 'bb', 'cc']
# new_list = '...'.join(list1)
# print(new_list)

"""
    字符串大小写修改
    capitalize()  字符串首字母大写
    title()       将字符串中每个单词的首字母大写
    lower()       大写变小写
    upper()       小写变大写  
"""
# str1 = 'then I have and passion and the and of handwriting'
#
# print(str1.capitalize())
# print(str1.title())
# print(str1.lower())
# print(str1.upper())
"""
    字符串删除左右的空白
    lstrip(）       删除左侧空白
    rstrip()        删除右侧空白
    strip()         删除左右两侧空白
"""
# str1 = '    then I have and passion and the and of handwriting    '
#
# print(str1.lstrip())
# print(str1.rstrip())
# print(str1.strip())
"""
    补齐字符长度，按自己所选定过的符号
    ljust()
    rjust()
    center()
"""
# str1 = 'hello'
#
# print(str1.ljust(10, '*'))
# print(str1.rjust(10, '*'))
# print(str1.center(10, '*'))

"""
    判断开头与结尾的字符
    startswith()  开头字符
    endswith()     结尾字符
"""

# str1 = 'then I have and passion and the and of handwriting'

# print(str1.startswith('then', 10, 20))
# print(str1.endswith('g'))

"""
    判断字符串由什么组成
    isalpha()       是否全是字母
    isdigit()       是否全是数字
    isalnum()       是否由字母和数字组成
    isspace()       是否全由空格组成
"""
# str1 = 'ds231salsa'
# print(str1.isalpha())

# str1 = '5445hgf4'
# print(str1.isdigit())

# str1 = 'dada4564'
# print(str1.isalnum())

# str1 = '  ds   '
# print(str1.isspace())



