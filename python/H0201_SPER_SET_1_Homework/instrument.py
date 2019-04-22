# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:35:05 2019

@author: taiki
"""

print('What is your name?')
name = input()

print ('Do you like music? Yes, or No ')
answer = input()
if answer == 'Yes' or answer == 'yes':

    print ('What kind of instrument do you like?')
    instrument = input()
    
    print(' Name:', name,'\n',
          'Likes Music:',answer,'\n',
          'Instrument Preference:',instrument,)

else:
    print('What do you listen inside the car?')
    car = input()
    
    print(' Name:', name,'\n',
          'Likes Music:',answer,'\n',
          'Activity During Travelling:',car,)