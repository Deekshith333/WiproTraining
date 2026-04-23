#
# #calculations pgm
#
# #functions
# def add(n1, n2):
#     return n1 + n2
#
# def sub(n1, n2):
#     return n1 - n2
#
# def mul(n1, n2):
#     return n1 * n2
#
# def div()
#     pass
#
#
# #driver
# num1=int(input('Enter a number : '))
# num2=int(input('Enter another number : '))
#
# res = add(num1, num2)
# print('Addition : ', res)
#
# res = sub(num1, num2)
# print('Subtraction : ', res)
#
# res = mul(num1, num2)
# print('Mulltiplication : ', res)


#Arbitary

# def add(nums):
#     sum=0
#     for n in nums:
#         sum += n
#         return sum

# numbers = list()
# count = int(input('How many ? '))
#
# for _ in range(1, count+1):
#     numbers.append(int(input('No: ')))
# print(add(48,39))
# print(add(38,3,45))


#optional

# def add(n1, n2, n3=10):
#     return n1 + n2 + n3
#
# #driver
# num1=int(input('Enter a number : '))
# num2=int(input('Enter another number : '))
#
# print(add(num1, num2))
# print(add(num1, num2,  100))


#lambda

# num1=int(input('Enter a number : '))
# num2=int(input('Enter another number : '))
#
# add = lambda n1, n2 : n1 + n2
# print(add(num1, num2))

numbers = [1,2,3,4,5]

sq = lambda nums : [num * num for num in nums if num%2 == 0]
print(tuple(sq(numbers)))