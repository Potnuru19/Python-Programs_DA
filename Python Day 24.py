'''
Day 24 10/09/26

Exception Handling:
--> This is the way handing errors
--> we can write any number exception for one code written at try block

1. try
--> The try block, where we can write code which may contain error
syntax -->
try:
    code lines
    
2. except
--> this will handle error that are raised at try block
syntax --> except ErrorName:
except ErrorName:
    print("ErrorName")
eg
try:
    print(5/0)
    print(num)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')

try:
    print(num)
    print(5/0)
except ZeroDivisionError:
    print('Division by zero')
except NameError:
    print('Name Error')


3. else
--> The else block will only execute, if no error at try block

4. finally
--> This block will execute regardless with the error at try block
eg
try:
    print("Hello")
except ZeroDivisionError:
    print('Dvision by zero')
except NameError:
    print('Name Error')
else:
    print('No Error')
finally:
    print('End')

File Handling
--> The file handler is a object, which is used to create, update ,read , and delete...

modes:
r
w
a
x

with open('Python day 7.txt','r') as file:
    print(file.read())

with open('Python day 7.txt','w') as file:
    file.write('This is samitha, I am a data analyst trainee')





'''
with open('Python day 7.txt','r') as file:
    print(file.read())

with open('Python day 7.txt','w') as file:
    file.write('This is samitha, I am a data analyst trainee')
