# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 23:56:27 2019

@author: Ken_PC
"""


#Question3
input_string = input("Enter denominations separated by space: ")
N = int(input('Enter amount N: '))
denominations = input_string.split()
denominations = list(map(int,denominations))
print('You entered: ', denominations)
denominations.sort(reverse=True)


def test(denominations, N):
    for i in denominations:
        if N % i == 0:
            return True
        elif i == denominations[-1]:
            return False
        else:
            N = N % i


test(denominations, N)