# -*- coding: utf-8 -*-
"""
Created on Thu May  9 18:54:03 2019

@author: taikinaka
"""

for a in range(0,22,1):
    print('Taiki')
b = 0
for a in range(0,25,1):
    
    b = b + 2 
    print(b)
for a in range(0,22,1):
    print('Taiki')

for a in range(0,50): 
    if a % 2==1:
        print(a)

for a in range(1,31): 
    if a % 3==0:
        print(a)
for a in range(0,10):
    print('What is your name?')
    name = input()
    print('Hello',name)

for a in range(50,0,-1):
    print(a)

for n in range(1,10,2):
    print('I Love YoungWonks',n)

import random
import time
for a in range(0,10,1):
    print(random.randint(1,10))
    time.sleep(3)

a = 1
while a < 51:
    print(a)
    a = a + 1

a = 50
while a > 0:
    print(a)
    a = a - 1

a = 1
while a < 51:
    if 0 == a % 7:
        print(a)
    a = a + 1

print ('What is my name?')
name = input()
while name != 'Taiki':
    print ('What is my name?')
    name = input()

print('How many people are working in the farm?')
people = int(input())
print('On an average,how many boxes of strawberries are picked each farmworker in one day?')
box_one = int(input())
print('How many strawberries does each box of strawberries contain?')
box = int(input())
box = box_one * box
print('Number of strawberries picked by one worker in one day is ',box_one * box,'.')
print('Assuming an 8-hour work day, the average number of strawberries picked by a worker in one hour is ',box / 8)

print('How old are you?')
age = int(input())
if age >= 18:
    print('You are allowed to work.')
elif 13 < age < 18:
    print('What is your GPA?')
    GPA = float(input())
    if GPA > 3.5:
        print('You are allowerd to work.')
    else:
        print('You are not allowed to work.')
else:
    print('You are not allowed to work.')