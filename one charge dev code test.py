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


#Question2
s = input('Please enter a string: ')
s = s[::-1]
print(s)


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


