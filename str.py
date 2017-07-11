print("hello world")
>>> a = {1,2,3,4}
>>> b ={3,4,5,6}
>>> a
{1, 2, 3, 4}
>>> type(a)
<class 'set'>
>>> a.symmetric_difference(b)
{1, 2, 5, 6}
>>> b.symmetric_difference(a)
{1, 2, 5, 6}
>>>
>>>
>>> a.difference(b)
{1, 2}
>>> a.union(b)
{1, 2, 3, 4, 5, 6}
>>> a.issu
a.issubset(   a.issuperset(
>>> a.issubset(b)
False
