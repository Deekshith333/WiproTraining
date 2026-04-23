"""
Date:21-04-26
Desc: different types of if stmt formats
"""

#big2
# num1 = int(input('Enter a number : '))
# num2 = int(input('Enter another number : '))
# if num1 == num2:
#     print('Both are equal')
# elif num1 > num2 :
#     print(num1, 'is big')
# else:
#     print(num2, 'is big')

#big3
# num1 = int(input('Enter a number : '))
# num2 = int(input('Enter another number : '))
# num3 = int(input('Enter another number : '))
#
# if num1 == num2 == num3:
#     print('All are equal')
# elif num1>num2 and num1>num3:
#     print(num1, 'is big')
# elif num2 > num1 and num2 > num3:
#     print(num2, 'is big')
# elif num3 > num1 and num3 > num1:
#     print(num3, 'is big')

#weekday
ch=int(input('Enter a number between 1 to 7 : '))

match(ch):
    case 1:
        print('monday')
    case 2:
        print('tuesday')
    case 3:
        print('wednesday')
    case 4:
        print('thursday')
    case 5:
        print('friday')
    case 6:
        print ('saturday')
    case 7:
        print('sunday')
    case _:
        print("invalid choice")