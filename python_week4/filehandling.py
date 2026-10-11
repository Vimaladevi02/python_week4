         
import os
os.chdir(os.path.expanduser("~/Documents"))
f = open("test.txt", "r")
f.close()
f
<_io.TextIOWrapper name='test.txt' mode='r' encoding='cp1252'>
f = open("test.txt", "r")
f.close()
f.readline()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    f.readline()
ValueError: I/O operation on closed file.
f = open("test.txt", "r")
f.readline()
'don\n'
f.readline()
'leo\n'
f.readline()
'kanchana\n'
f.readline()
'34\n'
f.close()
f = open("test.txt", "r")
for i in f.readlines():
    print(i)

    
don

leo

kanchana

34

lion
f.close()
f = open("test.txt", "w+")

f
<_io.TextIOWrapper name='test.txt' mode='w+' encoding='cp1252'>

f.write('school\ncollege\npen')
18
f.close()f = open("test.txt", "r")
SyntaxError: invalid syntax
f = open("test.txt", "r")
f.readlines()
['school\n', 'college\n', 'pen']
f.close()
with open('test.txt","a") as f:
          
SyntaxError: unterminated string literal (detected at line 1)
with open("test.txt","a") as f:
          f.writelines('pencil\nbottle')

      
f = open("test.txt", "r")
          
f.tell()
          
0
f.read(6)
          
'school'
f.tel()
          
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    f.tel()
AttributeError: '_io.TextIOWrapper' object has no attribute 'tel'. Did you mean: 'tell'?
f.tel1()
          
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    f.tel1()
AttributeError: '_io.TextIOWrapper' object has no attribute 'tel1'. Did you mean: 'tell'?
f.tel1()
          
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    f.tel1()
AttributeError: '_io.TextIOWrapper' object has no attribute 'tel1'. Did you mean: 'tell'?
f.tell()
          
6
f.seek(7)
          
7
f.tell()
          
7
f.close()
          
def angle():
    f=open("test.txt","w+")
    for i in range(0,6):
        for j in range(i):
            f.write(str(i))
        f.write('\n')
    f.close()

    
angle()


