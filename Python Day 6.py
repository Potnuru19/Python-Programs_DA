'''
Day 6

Strings

---------

Operations

1.Indexing --> getting the character
Indexing is used to get char that you looking to access  

Syntax -- from oth position we have to count
text = 'Python'
print(text[3])
print(text[-3])

Two Types
1.positive indexing (with space we have to count from 0)
positive indexing starts from 0 index
syntax --> print(variable_name[index_position])
eg
text = 'Python'
print(text[3])

2.negative indexing ( with space we have to count from -1)
negative indexing starts from -1 index
syntax --> print(variable_name[negative index_position])
eg
text = 'Python'
print(text[-3])

len()
len() is built in function that is used get number of char present in the string
syntax --> len(variable_name)\
eg
txt = 'Python is a programming language'
print(len(txt))
`
slicing --> -1 means reversing ::-1, ::-2 means skip one variable and reverse
this is used to access the particular part from string
syntax --> variable_name[start:end]
eg
txt = 'Python is a programming language'
print(txt[12:])
print(txt[:23])
print(txt[12:23])
rev = txt[::-1}
print(txt[::-1])

upper()
used to convert all small char into cap
txt = 'Python is a programming lamgauge'
print(txt.upper())
same for lower --> used to convert all cap into small
print(txt.lower())
eg
txt = 'PYTHON'
print(txt.lower())

index() --> getting the position
used to know the index position of an char
syntax--> variable_name.index('substring', start, end)
eg
txt = 'python is a programming language'
print(text.index(i))
print(text[7])

replace()

sub string
txt = 'Python is a Programming Language'
print(txt.index('x',2,15)

replace()
used to replace old substring with new substring
syntax --> variable_name.replace(old,new)
eg
txt = 'Python is programming language'
print(txt.replace('Python','Java'))

split()
this method is used to separate the string based on given substring
syntax --> variable_name.split(substring)
eg
txt = 'Python is a programming language'
print(txt.split(' '))

count()
used to count number of occurrences of an substring
syntax--> variable_name.count('substring')
eg
txt = 'Python is a programming language'
print(txt.count('a',1,12))


'''

