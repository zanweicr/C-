# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/01/08 10:44
# @Author  : makabaka
# @Version : python3.9
# @File    : while 
#
# i = 0
# while i < 5:
#     print('你好')
#     i += 1

# i = 0
#
# result = 0
#
# while i <= 100:
#     result += i
#     i += 1
#
# print(result)
#
# i = 0
#
# result = 0
#
# while i <= 100:
#     result += i
#     i += 2
#
# print(result)

# i = 0
#
# result = 0
#
# while i <= 8:
#     if i % 2 == 0:
#         result += i
#     i += 1
#
# print(result)

# i = 1
#
# while i <= 5:
#     if i == 3:
#         print(f'娘的，第{i}个苹果有虫子')
#         i += 1
#         continue
#     print(f'吃了{i}个苹果')
#     i += 1


# i = 1
#
# while i <= 5:
#     if i > 3:
#         print('吃饱了，爷不吃了')
#         i += 1
#         break
#     print(f'吃了{i}个苹果')
#     i += 1

"""
打印*
一行 5个，一共打印5列
"""

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 5:
#         print('*', end='')
#         j += 1
#     i += 1
#     print()

# i = 1
# while i <= 5:
#     j = 1
#     while j <= i:
#         print('*', end='')
#         j += 1
#     i += 1
#     print()


"""
打印九九乘法表 i * j = x
"""
i = 1

while i <= 9:
    j = 1
    while j <= i:
        print(f'{j} * {i} = {i * j}', end='\t')
        j += 1
    print()
    i += 1
