mytuple = ("apple", "banana", "cherry")


thistuple = ("apple", "banana", "cherry")
print(thistuple)

#('apple', 'banana', 'cherry')


thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#('apple', 'banana', 'cherry', 'apple', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

#3

thistuple = ("apple",)
print(type(thistuple))

#<class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#<class 'str'>

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)