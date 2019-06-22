#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:34:35 2019

@author: taikinaka
"""

friend = {
       'Kouki' : 'pees cream',
       'Taiki' : 'gum',
       'Masako' : 'chocolate',
       'Masashi' : 'peanuts'}
for a in friend:
    print(friend[a])
friend.pop('Taiki')
print(friend)