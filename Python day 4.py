'''

Day 4

*** Concatination
The + will behave two ways for numerics it works normally and for other datatypes like string, list, tuple it concatinates

Operators
The opearators are used to perform operations in variables and the values.
1.Arithematic Operator
+, -, *, / , // , %
+ --> to add the values
num = 90
num_2 = 7
print(num + num_2)

- sub
a = 9
b = 7
print(a - b)

* multiplication
v = 8
n = 4
print(v * n)

/ division
v = 8
n = 4
print(v / n)

// floor divison
n = 8.6
n = 4.7
print(v // n)

2.Assignment Operator
=, +=, -=, *=, %=, /=

+= --> is increment operator
a = 0
print(a)
a += 1
print(a)

-= -->  decrement operator
b = 7
b -= 5
print(b)

*=
c = 7
c *= 2
print(c)

%=
d = 7
d %= 2
print(d)

/=
e = 5
e /= 7
print(e)

3.Comaprison Operator
==, >=, <=, >, < ,!=

==
num = 9
num_2 = 5
print(num == num_2)# 9 == 5

!=
num = 9
num_2 = 5
print(num != num_2)#9 != 5

>
num = 9
num_2 = 5
print(num > num_2)#9 > 5

<
num = 9
num_2 = 5
print(num < num_2)#9 < 5

>=
num = 10
num_2 = 9
print(num >= num_2)

<=
num = 10
num_2 = 9
print(num <= num_2)

4.Logical Operator
and --> both values should be true then the output is true, if one is false then the output is false
num = 9
num_2 = 13
print(num >= num_2 and num <= 10)# 9 >= 13 and 9 <= 10
print(num <= num_2 and num <= 10)# 9 <= 13 and 9 <= 10

or --> left or right is true then the output is true
num = 9
num_2 = 13
print(num >= num_2 or num < 10)

not --> gives the opposite output
num = 9
num_2 = 13
print(not(num >= num_2 or num < 10))

5.Identity Operator
is --> it checks the only outer values , it will not check the values which is inside the brackets
locations (object) checking
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is b)

is not --> gives the opposite output od is
a = [1,2]
b = [1,2]
print(id(a))
print(id(b))
print(a is not b)

6.Membership Operator
in --> particular variable is there in that datatype or not
nums = 'python is a language'
print('y' in nums)

not in --> condition satisfy
nums = 'python is a language'
print('i' not in nums)

'''
