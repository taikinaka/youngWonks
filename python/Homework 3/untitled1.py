#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 17:50:16 2019

@author: taikinaka
"""

l = ['Apple','Banana','Orange','Strawberry','Mango','Lemon']
l.pop()
l.append('Blueberries')
l.pop(2)
l.insert(2,'Watermelon')
l.append('apple')
l.remove('apple')
for a in range(0,6):
    print(l[a])