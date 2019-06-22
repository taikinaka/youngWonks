#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:25:27 2019

@author: taikinaka
"""

friends=['Shunsuke','Haruki','Mukuto','Tomoya','Taiki']
a = len(friends)
print(a)
print(friends[2:5])
friends[4] = 'mathew'
print(friends)

a = -120
while 120>=a:    
    print(a)
    a = a + 1
b = 20
print( )
while 0<=b:
    print(b)
    b = b - 1
while b <= 35:
    print(b)
    b = b + 1
c = -17
print( )
while c <= 25:
    print(c)
    c = c + 1
while c >= 25 - 8:
    print(c)
    c = c - 1
print( )


#__________________________________
import time
from time import sleep
from random import randint
while True:
    print(randint(-99999999,99999999))
    time.sleep(3)

a = 20
time.sleep(1)
while a > 0:
    print(a)
    a = a - 1
    time.sleep(1)
print('BLAST OFF!')