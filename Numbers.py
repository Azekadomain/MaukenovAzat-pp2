x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#<class 'int'>
#<class 'int'>
#<class 'int'>

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#<class 'float'>
#<class 'float'>
#<class 'float'>

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#<class 'float'>
#<class 'float'>
#<class 'float'>


x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#<class 'complex'>
#<class 'complex'>
#<class 'complex'>

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
#1.0

print(b)
#2

print(c)
#(1+0j)

print(type(a))
#<class 'float'>

print(type(b))
#<class 'int'>

print(type(c))
#<class 'complex'>

import random

print(random.randrange(1, 10))