#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 16:59:12 2019

@author: taikinaka
"""
#
#for a in range(1,23,1):
#    print(a,'Taiki')
import random
import time
from random import randint

print('how much money do you have?')
money = int(input())
while money > 0:
    print('Do you want to roll the dice?')
    decide = input()
    if decide[0] == 'y' or decide[0] == 'Y':
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        print('waiting a few seconds...')
        time.sleep(2)
        if int(dice1) == int(dice2):
            print('It mached!! By ',dice1,'and ',dice2,'.')
            money = money + 5
            print('money:',money)
        else:
            print('It didn\'t mached. By ',dice1,'and ',dice2,'.')
            money = int(money) - 1
            print('money:',money)
    else:
        print('Come back here right now!!!!')
        break
print('Sorry you don\'t have enough money to play...')