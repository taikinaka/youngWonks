# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import random
from colorama import Fore
from Color import *
from colorama import Style
print( )
print( ) 
print( )
print( ) 
print(Fore.BLUE + '                           Math Quiz Game')
print(GColor.RGB(0,0,102) + 'Addition Subtraction Multiplication Division please capitalized')
choice = input()
Score=0
if choice == 'Addition':
    print('Easy Medium Difficult')
    Level = input()
    if Level == 'Easy':
        print(Fore.GREEN + 'Addition Level Easy')
        for a in range (0,10,1):
            E_Add = random.randint(1,15)
            number1 = E_Add
            E_Add = random.randint(1,15)
            number2 = E_Add
            answer = number1 + number2
            print('Question',a + 1,': ',number1, ' + ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print(GColor.RGB(255,0,0),'You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(1,15)
                number1 = E_Add
                E_Add = random.randint(1,15)
                number2 = E_Add
                answer = number1 + number2
                print('Question',a + 1,': ',number1, ' + ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!' + Style.RESET_ALL)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif Level == 'Medium':
        print(GColor.RGB(255,128,0),'Addition Level Medium')
        for a in range (0,10,1):
            E_Add = random.randint(16,30)
            number1 = E_Add
            E_Add = random.randint(16,30)
            number2 = E_Add
            answer = number1 + number2
            print('Question',a + 1,': ',number1, ' + ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(16,30)
                number1 = E_Add
                E_Add = random.randint(16,30)
                number2 = E_Add
                answer = number1 + number2
                print('Question',a + 1,': ',number1, ' + ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print(GColor.RGB(204, 0, 0),'Addition Level Hard')
        for a in range (0,10,1):
            E_Add = random.randint(50,100)
            number1 = E_Add
            E_Add = random.randint(50,100)
            number2 = E_Add
            answer = number1 + number2
            print('Question',a + 1,': ',number1, ' + ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(50,100)
                number1 = E_Add
                E_Add = random.randint(50,100)
                number2 = E_Add
                answer = number1 + number2
                print('Question',a + 1,': ',number1, ' + ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
elif choice == 'Subtraction':
    print('Easy Medium Difficult')
    Level = input()
    if Level == 'Easy':
        print(Fore.GREEN + 'Subtraction Level Easy')
        for a in range (0,10,1):
            E_Add = random.randint(10,15)
            number1 = E_Add
            E_Add = random.randint(1,10)
            number2 = E_Add
            answer = number1 - number2
            print('Question',a + 1,': ',number1, ' - ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(10,15)
                number1 = E_Add
                E_Add = random.randint(1,10)
                number2 = E_Add
                answer = number1 - number2
                print('Question',a + 1,': ',number1, ' - ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                        print('Correct!')
                        Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!' + Style.RESET_ALL)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif Level == 'Medium':
        print(GColor.RGB(255,128,0),'Subtraction Level Medium')
        for a in range (0,10,1):
            E_Add = random.randint(20,30)
            number1 = E_Add
            E_Add = random.randint(10,20)
            number2 = E_Add
            answer = number1 - number2
            print('Question',a + 1,': ',number1, ' - ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(20,30)
                number1 = E_Add
                E_Add = random.randint(10,20)
                number2 = E_Add
                answer = number1 - number2
                print('Question',a + 1,': ',number1, ' - ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print(GColor.RGB(204, 0, 0),'Subtraction Level Difficult')
        for a in range (0,10,1):
            E_Add = random.randint(80,100)
            number1 = E_Add
            E_Add = random.randint(50,80)
            number2 = E_Add
            answer = number1 - number2
            print('Question',a + 1,': ',number1, ' - ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(80,100)
                number1 = E_Add
                E_Add = random.randint(50,80)
                number2 = E_Add
                answer = number1 - number2
                print('Question',a + 1,': ',number1, ' - ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
elif choice == 'Multiplication':
    print('Easy Medium Difficult')
    Level = input()
    if Level == 'Easy':
        print(Fore.GREEN + 'Multiplication Level Easy')
        for a in range (0,10,1):
            E_Add = random.randint(1,5)
            number1 = E_Add
            E_Add = random.randint(1,5)
            number2 = E_Add
            answer = number1 * number2
            print('Question',a + 1,': ',number1, ' x ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(1,5)
                number1 = E_Add
                E_Add = random.randint(1,5)
                number2 = E_Add
                answer = number1 * number2
                print('Question',a + 1,': ',number1, ' x ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!' + Style.RESET_ALL)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif Level == 'Medium':
        print(GColor.RGB(255,128,0),'Multiplication Level Medium')
        for a in range (0,10,1):
            E_Add = random.randint(5,10)
            number1 = E_Add
            E_Add = random.randint(5,10)
            number2 = E_Add
            answer = number1 * number2
            print('Question',a + 1,': ',number1, ' x ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(5,10)
                number1 = E_Add
                E_Add = random.randint(5,10)
                number2 = E_Add
                answer = number1 * number2
                print('Question',a + 1,': ',number1, ' x ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print(GColor.RGB(204, 0, 0),'Multiplication Level Difficult')
        for a in range (0,10,1):
            E_Add = random.randint(20,50)
            number1 = E_Add
            E_Add = random.randint(20,50)
            number2 = E_Add
            answer = number1 * number2
            print('Question',a + 1,': ',number1, ' x ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                E_Add = random.randint(20,50)
                number1 = E_Add
                E_Add = random.randint(20,50)
                number2 = E_Add
                answer = number1 * number2
                print('Question',a + 1,': ',number1, ' x ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
else:
    print('Easy Medium Difficult')
    Level = input()
    if Level == 'Easy':
        print(Fore.GREEN + 'Division Level Easy')
        for a in range (0,10,1):
            dividends = [6,12,18,24,30,36]
            number1 = dividends[random.randint(0,5)]
            divisors = [3,6]
            number2 = random.choice(divisors)
            answer = number1 / number2
            print('Question',a + 1,': ',number1, ' / ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                dividends = [6,12,18,24,30,36]
                number1 = dividends[random.randint(0,5)]
                divisors = [3,6]
                number2 = random.choice(divisors)
                answer = number1 / number2
                print('Question',a + 1,': ',number1, ' / ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!' + Style.RESET_ALL)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif Level == 'Medium':
        print(GColor.RGB(255,128,0),'Division Level Medium')
        for a in range (0,10,1):
            dividends = [14,28,42,56,70,84,98]
            number1 = dividends[random.randint(0,6)]
            divisors = [7,14]
            number2 = random.choice(divisors)
            answer = number1 / number2
            print('Question',a + 1,': ',number1, ' / ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (0,10,1):
                dividends = [14,28,42,56,70,84,98]
                number1 = dividends[random.randint(0,6)]
                divisors = [7,14]
                number2 = random.choice(divisors)
                answer = number1 / number2
                print('Question',a + 1,': ',number1, ' / ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print(GColor.RGB(204, 0, 0),'Division Level Difficult')
        for a in range (10):
            dividend = random.choice([16,32,48,64,80,96,112,128,144,160,176,192])
            divisor = random.choice([8,16])
            answer = dividend / divisor
            print('Question',a + 1,': ',dividend, ' / ' ,divisor)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        if int(Score) == 10:
            print(' ')
            print(' ')
            print('10 more!')
            print(' ')
            for a in range (10):
                dividend = random.choice([16,32,48,64,80,96,112,128,144,160,176,192])
                divisor = random.choice([8,16])
                answer = dividend / divisor
                print('Question',a + 1,': ',dividend, ' / ' ,divisor)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/20!',GColor.END)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        