thisdict = {
  "first":  "one",
  "second":  "two",
  "third":  "three"
}

for x in thisdict:
  print(x)

  '''
first
second
third
  '''

for x in thisdict.values():
  print(x)

'''
one
two
three
'''

for x in thisdict.keys():
  print(x)

'''
first
second
third
'''

for x, y in thisdict.items():
  print(x, y)

'''
first one
second two
third three
'''