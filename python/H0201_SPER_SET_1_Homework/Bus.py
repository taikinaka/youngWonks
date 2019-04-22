# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print('Approximately how many students are there in each grade?')

numberOfStudentsPerGrade = input()

print('How many grades are going for the field trip?')

numberOfGrades = input()

print('What is the maximum capacity of each bus?')

busCapacity = input()

numberOfBuses = int(numberOfStudentsPerGrade) * int(numberOfGrades) /  int(busCapacity)

numberOfStudents = int(numberOfStudentsPerGrade) * int(numberOfGrades)

numberOfBuses = int(numberOfBuses)

print('A total of',numberOfStudents, 'students will be going for the field trip.', numberOfBuses, 'buses will be needed.' )

