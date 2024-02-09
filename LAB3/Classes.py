#1
class string:
    def __init__(self):
        self.my_string =""
    def getString(self):
        self.my_string = input()
    def printString(self):
        print (self.my_string.upper())
#my_string_obj = string()
#my_string_obj.getString()
#my_string_obj.printString()

#2
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2
square1 = Square(5)
shape2 = Shape()
#print(square1.area())
#print(shape2.area())

#3
class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
rectangle1 = Rectangle(10, 5)
#print(rectangle1.area())  

#4
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"coordinates: ({self.x} {self.y})")
    def move(self,dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def dist(self, second_point):
        return math.sqrt( (self.x - second_point.x)**2 + (self.y - second_point.y)**2 )

#point1 = Point(3, 4)
#point2 = Point(7, 9)

#point1.show()

#point1.move(2, 3)
#point1.show()

#print(point1.dist(point2))

#5
class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self,cash):
        if cash > 0:
            self.balance = self.balance + cash
            print (f"the operation to deposit {cash} tenge was successful")
        else:
            print("you must deposit more than 0 tenge")
    def withdraw(self,mycash):
        if mycash <= self.balance:
            self.balance = self.balance - mycash
            print (f"you withdrew money in the amount of {mycash} tenge")
        else:
            print ("insufficient funds")

#bank = Bank("hmm", 570)
#bank.deposit(30)
#bank.withdraw(700)
#bank.deposit(100)
#bank.withdraw(700)
            
#6
def prime(num):
    num = int(num)
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

#numbers = input().split()
#prime_numbers = list(filter(lambda x: prime(x), numbers))
#print(*prime_numbers)