# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:55:07 2019

@author: Ken_PC
"""

#Question1
n = int(input('Number of kids: '))


for i in range(1,n):
    multiple = False
    if i % 3 == 0:
        print('Fizz',end=' ')
        multiple = True
    if i % 5 == 0:
        print('Buzz',end=' ')
        multiple = True
    if i % 7 == 0:
        print('Woof', end=' ')
        multiple = True
    if multiple == False:
        print(i)
    else:
        print()







