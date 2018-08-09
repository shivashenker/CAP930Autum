Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a=42
>>> a
42
>>> print(str(a))
42
>>> typr a
SyntaxError: invalid syntax
>>> type(a)
<class 'int'>
>>> print(str(a))
42
>>> type(a)
<class 'int'>
>>> print(type(str(a)))
<class 'str'>
>>> str(42)
'42'
>>> int("42")
42
>>> float("2.5")
2.5
>>> a=str(42)
>>> a
'42'
>>> type(a)
<class 'str'>
>>> b=float("1")
>>> b
1.0
>>> type(b)
<class 'float'>
>>> easy_as=[1,2,3]
>>> as
SyntaxError: invalid syntax
>>> print(as)
SyntaxError: invalid syntax
>>> easy
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    easy
NameError: name 'easy' is not defined
>>> easy_as
[1, 2, 3]
>>> empty[]
SyntaxError: invalid syntax
>>> empty=[]
>>> empty
[]
>>> letters = ['a','b','c','d']
>>> letters
['a', 'b', 'c', 'd']
>>> mixed[4,5,secounds]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    mixed[4,5,secounds]
NameError: name 'mixed' is not defined
>>> mixed=[4,5]
>>> mixed
[4, 5]
>>> letters=[a,b,c,d]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    letters=[a,b,c,d]
NameError: name 'c' is not defined
>>> a=[1,2,3,4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]
>>> a[0]
1
>>> a[1:-1]
[2, 3, 4]
>>> a[:3]
[1, 2, 3]
>>> a[:2]
[1, 2]
>>> a=[1,2,3,4]
>>> b=['a','b','c','d']
>>> Nested_Lsit=[a,b]
>>> Nedted_List
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    Nedted_List
NameError: name 'Nedted_List' is not defined
>>> Nested_List
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    Nested_List
NameError: name 'Nested_List' is not defined
>>> Nested_Lsit
[[1, 2, 3, 4], ['a', 'b', 'c', 'd']]
>>> 
