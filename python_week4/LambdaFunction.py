highest_age=lambda a,b,c: a if a>b and a>c else b if b>c else c
highest_age(40,30,10)
40
#Types
#Map
s= [1,2,3,4,5]
c=list(map(lambda a : a**2,s))
print(c)
[1, 4, 9, 16, 25]
#Filter
t=[1,2,3,4,5,6,7,8,9,10]
a=list(filter(lambda a : a%2==0, t))
print(a)
[2, 4, 6, 8, 10]
#reduce
from functools import reduce
r=[1,2,3,4,5,6,7,8,9,10]
r=reduce(lambda a,b:a+b,r)
print(r)
55

