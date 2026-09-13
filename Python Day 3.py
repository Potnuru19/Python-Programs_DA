'''
Day 3

Datatypes & TypeConversions
1.Numeric Datatype
  Float and integer is called as numeric datatype

Float
A number which contains decimal values, we call it as a float datatype
eg
56.89
price = 56.89

integer (int)
A normal number without any decimal values
eg
num = 89
num_2 = 6

2.String
String is a sequence of char that are enclosed in '',"",""""""
String is immutable
eg
any_ = 'Python is a language'
all_ = 'Ab,.&[)-+'

3.List
List is a collection of different datatypes
and it is represented by [] that are separated by ,
inside the list we call it as items
list is mutable
eg
any_ = [1,'Python',[5,6]]
print(type(any_))

4.Tuple
tuple is collection of different datatypes that are enclose in () and those are separated by ,
tuple is immutable
eg
nums = (1,89.67, 'Python',[3,4].(8,9))

5.Dictionary
Dictionary is collection of key:value pairs , keys and values are separated by :
key and value pair is call it as a item
and this items are separated by ,
Dictionary is represent using {}
in  key place we can use immutable datatypes
in values place we can use any datatype
eg
data_ = {1:2,
         'name':'Teja',
         (2,3):'Tuple'}
print(data_)

6.Set
set is collection unique elements and set can't allow any duplicate values inside it.....
set is represented by {} and the elements are separated by ,
an = {1,2,3}
print(an)

Type Conversion

float --> int, str
eg --> int
price = 45.78
print(int(price))

--> str()
price = 45.78
con = str(price)
print(type(con))

integer --> float, str
eg --> float()
num = 78
print(float(num))

--> str()
num = 78
con_ = str(num)
print(type(con_))

string --> int, float
eg --> int()
do = '3456'
print(int(do))

-->float()
do = '10.89'
print(float(do))

list --> tuple, string
eg --> tuple()
nums = [1,2,3,4]
print(tuple(nums))

eg
tuple --> list
eg --> list()
all_ = (5,6,7)
print(list(all_))

set --> tuple, list
eg --> tuple()
all_ = {5,6,7}
print(tuple(all_))

dictionary --> list
eg --> dict()

details = [('name','samitha'),('edu','Mca')]
print(dict(details))






'''
