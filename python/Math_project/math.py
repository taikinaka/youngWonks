# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import random
print( )
print( ) 
print( )
print( ) 
print( )
print( ) 
print( )
print( ) 
print( )

print('                           Math Quiz Game')
print('Addtion Subtraction Multiplication Division please capitalized')
choice = input()
Score=0
if choice == 'Addtion':
    print('Easy Medium Difficult (Their is 10 questions.)')
    Level = input()
    if Level == 'Easy':
        print('Addtion Level Easy')
        for a in range (0,10,1):
            E_Add = random.randint(1,15)
            number1 = E_Add
            E_Add = random.randint(1,15)
            number2 = E_Add
            answer = number1 + number2
            print('Question',a,': ',number1, ' + ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif Level == 'Medium':
        print('Addtion Level Easy')
        for a in range (0,10,1):
            E_Add = random.randint(16,30)
            number1 = E_Add
            E_Add = random.randint(16,30)
            number2 = E_Add
            answer = number1 + number2
            print('Question',a,': ',number1, ' + ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print('Addtion Level Hard')
        for a in range (0,10,1):
            E_Add = random.randint(50,100)
            number1 = E_Add
            E_Add = random.randint(50,100)
            number2 = E_Add
            answer = number1 + number2
            print('Question',a,': ',number1, ' + ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
elif choice == 'Subtraction':
    print('Easy Medium Difficult(Their is 10 questions.)')
    Level = input()
    if Level == 'Easy':
        print('Subtraction Level Easy')
        for a in range (0,10,1):
            E_Add = random.randint(10,15)
            number1 = E_Add
            E_Add = random.randint(1,10)
            number2 = E_Add
            answer = number1 - number2
            print('Question',a,': ',number1, ' - ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if Level == 'Medium':
            print('Subtraction Level Medium')
            for a in range (0,10,1):
                E_Add = random.randint(20,30)
                number1 = E_Add
                E_Add = random.randint(10,20)
                number2 = E_Add
                answer = number1 - number2
                print('Question',a,': ',number1, ' - ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
            print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        else:
            print('Subtraction Level Difficult')
            for a in range (0,10,1):
                E_Add = random.randint(80,100)
                number1 = E_Add
                E_Add = random.randint(50,80)
                number2 = E_Add
                answer = number1 - number2
                print('Question',a,': ',number1, ' - ' ,number2)
                pearson_answer = int(input())
                if answer == pearson_answer:
                    print('Correct!')
                    Score=Score+1
                else:
                    print('Wrong!')
                print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
elif choice == 'Multiplication':
    print('Easy Medium Difficult(Their is 10 questions.)')
    Level = input()
    if Level == 'Easy':
        print('Multiplication Level Easy')
        for a in range (0,10,1):
            E_Add = random.randint(1,5)
            number1 = E_Add
            E_Add = random.randint(1,5)
            number2 = E_Add
            answer = number1 * number2
            print('Question',a,': ',number1, ' x ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif Level == 'Medium':
        print('Multiplication Level Medium')
        for a in range (0,10,1):
            E_Add = random.randint(5,10)
            number1 = E_Add
            E_Add = random.randint(5,10)
            number2 = E_Add
            answer = number1 * number2
            print('Question',a,': ',number1, ' x ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print('Multiplication Level Difficult')
        for a in range (0,10,1):
            E_Add = random.randint(20,50)
            number1 = E_Add
            E_Add = random.randint(20,50)
            number2 = E_Add
            answer = number1 * number2
            print('Question',a,': ',number1, ' x ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
            print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
else:
    print('Easy Medium Difficult')
    Level = input()
    if Level == 'Easy':
        print('Division Level Easy(Their is 10 questions.)')
        for a in range (0,10,1):
            dividends = [6,12,18,24,30,36]
            number1 = dividends[random.randint(0,5)]
            divisors = [3,6]
            number2 = random.choice(divisors)
            answer = number1 / number2
            print('Question',a,': ',number1, ' / ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    elif Level == 'Medium':
        print('Division Level Medium')
        for a in range (0,10,1):
            dividends = [14,28,42,56,70,84,98]
            number1 = dividends[random.randint(0,6)]
            divisors = [7,14]
            number2 = random.choice(divisors)
            answer = number1 / number2
            print('Question',a,': ',number1, ' / ' ,number2)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
        print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    else:
        print('Division Level Difficult')
        for a in range (10):
        
            dividend = random.choice([16,32,48,64,80,96,112,128,144,160,176,192])
            divisor = random.choice([8,16])
            answer = dividend / divisor
            print('Question',a,': ',dividend, ' / ' ,divisor)
            pearson_answer = int(input())
            if answer == pearson_answer:
                print('Correct!')
                Score=Score+1
            else:
                print('Wrong!')
            print('You got ',Score,'/10!')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~