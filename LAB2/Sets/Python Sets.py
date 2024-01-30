thisset = {"apple", "banana", "cherry"}
print(thisset)

#{'apple', 'banana', 'cherry'}

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#{'banana', 'cherry', 'apple'}

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

#{True, 2, 'apple', 'banana', 'cherry'}

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)

#{False, 'cherry', True, 'banana', 'apple'}

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#3

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))

#<class 'set'>

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#{'banana', 'apple', 'cherry'}