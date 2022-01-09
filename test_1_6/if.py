# !/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/01/06 13:17
# @Author  : makabaka
# @Version : python3.9
# @File    : if 

# print('请输入你的年龄:')
# age = int(input())
# if int(age) > 18:
#     print('可以上网')
# else:
#     print('不可以')


# # 获取招收人员的年龄
# age = int(i`nput('请输入您的年龄:'))
#
# # 年龄 <18 为童工
# if (age > 0) and (age < 18):
#     print(f'您的年龄为{age},我们这里不招收童工的')
# # 18---60岁 招收年龄
# elif 18 <= age <= 60:
#     print(f'您的年龄为{age}，刚刚好，正是我们招收的范围')
# # 60以上 退休年龄 不在招收
# elif age >= 60:
#     print(f'您的年龄为{age},已经到了退休的年纪，您可以享受清福')
# else:
#     print('您输入的年龄有误，请重新输入')
#
# Money = int(input('查看自己的钱包有多少钱:'))
#
# if Money > 0:
#     print('老板，请上车')
#     Seat = int(input('环顾四周看有几个空座:'))
#     if Seat > 0:
#         print('妈的，终于有座位了，可以让老子坐下了')
#     else:
#         print('我真服了，一个空座都没有')
# else:
#     print('没钱，慢慢等着吧')
# 单纯的做一个石头剪刀布的游戏

import random

player = int(input('请出拳: 0---石头  1---剪刀  2---布'))

computer = random.randint(0, 2)
print(computer)
if ((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print('玩家获胜')
elif player == computer:
    print('平局')
else:
    print('电脑获胜')
