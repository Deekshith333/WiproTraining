Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
s1
'hello'
type(s1)
<class 'str'>
s1.capitalize()
'Hello'
s1.upper()
'HELLO'
s1.lower()
'hello'
s1='hElLO'
s1
'hElLO'
s1.casefold()
'hello'
s1='HeLLo'
s1.lower()
'hello'
s1.count('l')
0
s1.count('L')
2
s1.endswith('o')
True
s1..ends
SyntaxError: invalid syntax
s1.endswith('O')SyntaxError: invalid syntax
SyntaxError: invalid syntax
s1.endswith('O')
False
s1.find('L')
2
s.find('l')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.find('l')
NameError: name 's' is not defined. Did you mean: 's1'?
s1.find('l')
-1
1.index('o')
SyntaxError: invalid syntax
s1.index('o')
4
s1.index('O')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s1.index('O')
ValueError: substring not found
s1.join('hi')
'hHeLLoi'
>>> s1.split()
['HeLLo']
>>> s1.replace('l','i')
'HeLLo'
>>> KeyboardInterrupt
>>> len(s1)
5
>>> s1[7]]
SyntaxError: unmatched ']'
>>> s1[7]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s1[7]
IndexError: string index out of range
>>> s1[-3]
'L'
>>> s1[1:4]
'eLL'
>>> s1[:]
'HeLLo'
>>> s1[0:5:2]
'HLo'
>>> s1[::3]
'HL'
>>> s1[::-2]
'oLH'
>>> s1[4::-2]
'oLH'
