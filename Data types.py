#Ex1
x = 5
print(type(x))
#<class 'int'>


#Ex2
x = "Hello World"
print(type(x))
#<class 'str'>

#Ex3
x = 20.5
print(type(x))
#<class 'float'>

#Ex4
x = 1j
print(type(x))
#<class 'complex'>

#EX5
x = ["apple", "banana", "cherry"]
print(type(x))
#<class 'list'>

#Ex6
x = ("apple", "banana", "cherry")
print(type(x))
#<class 'tuple'>

#Ex7
x = range(6)
print(type(x))
#<class 'range'>

#Ex8
x = {"name" : "John", "age" : 36}
print(type(x))
#<class 'dict'>

#Ex9
x = {"apple", "banana", "cherry"}
print(type(x))
#<class 'set'>

#Ex10
x = frozenset({"apple", "banana", "cherry"})
print(type(x))
#<class 'frozenset'>

#Ex11
x = True
print(type(x))
#<class 'bool'>

#Ex12
x = b"Hello"
print(type(x))
#<class 'bytes'>


#Ex13
x = bytearray(5)
print(type(x))
#<class 'bytearray'>

#Ex14
x = memoryview(bytes(5))
print(type(x))
#<class 'memoryview'>

#Ex15
x = None
print(type(x))
#<class 'NoneType'>