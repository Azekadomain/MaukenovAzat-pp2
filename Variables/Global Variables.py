x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
#Python is awesome


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
#Python is fantastic
#Python is awesome


def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Python is fantastic


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#Python is fantastic