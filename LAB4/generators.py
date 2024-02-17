#1
def generator(n):
    a = (i**2 for i in range(1,n+1))
    return a
#print(*generator(int(input())))

#2
def evens(n):
    a = (i for i in range(1,n) if i % 2 == 0)
    return a
#print(*evens(int(input())), sep=', ')

#3
def divisible(n):
    a = (i for i in range(n+1) if i % 3 == 0 and i % 4 == 0)
    return a
#print(*divisible(int(input())))

#4
def squares(a,b):
    for i in range(a,b+1):
        yield i**2
#print(*squares(int(input()), int(input())))

#5
def num_down(n):
    for i in range(n, -1, -1):
        yield i
#print(*num_down(int(input())))
