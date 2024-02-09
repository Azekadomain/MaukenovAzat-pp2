#1
def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces

#print(grams_to_ounces(34))

#2
def fahrenheit_to_centigrade(f):
    c = (5 / 9) * (f - 32)
    return c

#print(fahrenheit_to_centigrade(34))

#3
def solve(numheads, numlegs):
    numchick = 0
    numrab = 0
    for chicken in range(numheads):
        for rabbit in range(numheads):
            if chicken + rabbit == numheads and 2*chicken + 4*rabbit == numlegs:
                numchick = chicken
                numrab = rabbit
    return numchick, numrab
  
#print(solve(35, 94))

#4
from math import sqrt
def filter_prime(numbers):
    num_list = numbers.split()
    prime_list = []
    for num in num_list:
        i = int(num)
        div = 0
        for j in range(2,int(sqrt(i))+1):
            if i % j == 0:
                div += 1
        if div == 0:
            if i > 1:
                prime_list.append(i)
    return prime_list


#print(filter_prime(input()))   

#5

from itertools import permutations

def permutation(input):
    lis = [''.join(perm) for perm in permutations(input)]
    print(*lis)
    pass

#permutation(input()) 

#6
    
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


#print(reverse_words(input()))

#7

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#print(has_33([1, 3, 3]))  
#print(has_33([1, 3, 1, 3]))
#print(has_33([3, 1, 3]))

#8

def spy_game(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i+2] == 7:
            return True
    return False

#print(spy_game([1,2,4,0,0,7,5]))
#print(spy_game([1,0,2,4,0,5,7]))
#print(spy_game([1,7,2,0,4,5,0]))

#9

from math import pi
def volume_sphere(radius):
    volume = 4/3 * pi * radius**2
    return volume

#print(volume_sphere(int(input())))

#10

def unique_list(listt):
    new_list = []
    for i in range(len(listt)):
        if listt[i] not in new_list:
            new_list.append(listt[i])
    return new_list

#print(unique_list(input().split()))

#11

def is_polindrom(word):
    count = 0
    n = int(len(word)/2)+1
    for i in range(n):
        if word[i] == word[-i-1]:
            count += 1
    if count == n:
        return True
    return False
#print(is_polindrom(input()))
    

#12

def histogram(listt):
    for i in listt:
        print('*'*int(i), sep= '')
    pass



#histogram(input().split())
        
#13
        
import random
def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    secret = random.randint(1,20)
    guesses_taken = 0
    while True:
        print("Take a guess.")
        gues = int(input())
        guesses_taken += 1
        if gues < secret:
            print ("Your guess is too low.")
        elif gues > secret:
            print ("Your guess is too high")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break
#guess_the_number()