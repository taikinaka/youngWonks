#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 19 14:10:21 2019

@author: taikinaka
"""
#print('put key')

K = int(input())
print('')
#print('Put numbers')
prob = 0
print('put number')
N = int(input())

for a in range(1,N+1):
    p = 0
    num = a
    while(K >num):
        num=num*2
        #print('num=',num)
        p = p + 1
    #print("p=",p)
    prob = prob + 0.5**p
prob = prob/N
print(prob)