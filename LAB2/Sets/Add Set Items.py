thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#{'apple', 'orange', 'cherry', 'banana'}

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

#{'pineapple', 'cherry', 'papaya', 'banana', 'apple', 'mango'}

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#{'orange', 'apple', 'banana', 'cherry', 'kiwi'}