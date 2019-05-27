#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:31:17 2019

@author: taikinaka
"""

A,B = map(int, input().split())
if A >= 13:
    print(B)
elif 12 >= A > 5:
    print(int(B / 2))
else:
    print(0)