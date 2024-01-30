thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

'''
apple
banana
cherry
'''

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

'''
apple
banana
cherry
'''

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

'''
apple
banana
cherry
'''

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

'''
apple
banana
cherry
'''