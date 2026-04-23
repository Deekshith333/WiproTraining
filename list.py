Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s1='hello'
type(s1)
<class 'str'>
id(s1)
2861500610240
s2='hi'
id(s2)
140704778106296
s3=s1
id(s3)
2861500610240
s1='hi'
id(s1)
140704778106296
s2='where'
id(s2)
2861457912576

list1=[10,20,30,40]
list1
[10, 20, 30, 40]
type(list1)
<class 'list'>
list1[0]
10
list1[3]
40
list1[4]
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list1[4]
IndexError: list index out of range
list1[-1]
40
list1[0:3]
[10, 20, 30]
list1[0:3:2]
[10, 30]
list2=list('hi','hello')
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    list2=list('hi','hello')
TypeError: list expected at most 1 argument, got 2
s1
'hi'
list2=list(s1)
list1
[10, 20, 30, 40]
list2
['h', 'i']
list3=list1
id(list1)
2861503202176
id(list3)
2861503202176
list4['hi',40,'hello',true,69.69]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    list4['hi',40,'hello',true,69.69]
NameError: name 'list4' is not defined. Did you mean: 'list1'?
list4['hi',50,'hello',True,60.69]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list4['hi',50,'hello',True,60.69]
NameError: name 'list4' is not defined. Did you mean: 'list1'?
list4['hey',100,True,38,47.4]
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    list4['hey',100,True,38,47.4]
NameError: name 'list4' is not defined. Did you mean: 'list1'?
list4=['hi',50,'hello',True,60.69]
list4
['hi', 50, 'hello', True, 60.69]
>>> list4[5]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    list4[5]
IndexError: list index out of range
>>> list4[2]=35
>>> list4
['hi', 50, 35, True, 60.69]
>>> list4.append('hello')
>>> list4
['hi', 50, 35, True, 60.69, 'hello']
>>> list4.remove(50)
>>> list4
['hi', 35, True, 60.69, 'hello']
>>> list4.remove(38)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    list4.remove(38)
ValueError: list.remove(x): x not in list
>>> list4.pop()
'hello'
>>> list4
['hi', 35, True, 60.69]
>>> list4.pop(2)
True
>>> list4
['hi', 35, 60.69]
