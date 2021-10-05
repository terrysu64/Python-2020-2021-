#Author: Terry Su 

#Date: June 17, 2021
#Purpose: a coding sandbox to test out algorithms or datastructures

def reverse(s):
    
    if s == '':
        return ''
    
    return s[-1] + reverse(s[:-1])

def reverse2(s):
    return s[::-1]

def bubble_sort(arr): #bubble up largest values one by one
    
    count = len(arr) - 1
    
    while count != 0:
        
        for i in range(0,count):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

        count -= 1

    return arr

def selection_sort(arr): #find minimum values one by one and place them at front of array

    count = 0

    while count < len(arr):

        min_val = arr[count]

        for i in range(count,len(arr)):
            min_val = min(arr[i],min_val)

        min_index = arr.index(min_val)
        arr[count], arr[min_index] = arr[min_index],arr[count]

        count += 1

    return arr

def insertion_sort(arr): #rebuilding a sorted list within itself, one index at a time
                         #iterate through each index (starting with index:1) and find its respective position among previous indices

    for i in range(1,len(arr)):

        curr = arr[i]

        for j in range(0,i):
            if curr <= arr[j]:
                arr.insert(j,curr)
                arr.pop(i+1)
                break
                
    return arr

def fib(n):

    calculations = 0
    
    def calculate(n):
        
        nonlocal calculations
        # Defining a variable as non-local will cause it to bind
        # to the nearest non-global variable with the same name.
        calculations += 1
        
        if n <= 2:
            return 1

        return calculate(n-1) + calculate(n-2)

    return calculate(n), calculations

def dynamic_programming_fib(n): #optimized with memoization

    calculations = 0
    cache = {} #we could also put 'seen' in global scope at the sacrifice of global pollution

    def calculate(n):

        nonlocal calculations
        nonlocal cache

        calculations += 1

        if n in cache:
            return cache[n]

        if n <= 2:
            return 1

        cache[n] = calculate(n-1) + calculate(n-2)

        return cache[n]

    return calculate(n), calculations

def x():
    hi = 'hi'

    def y():
        nonlocal hi
        hi += 'a'
        print('hi')

    y()

x()

class test():

    def print_num(self):
        print(1+1)

    @staticmethod
    def method(x):
        print(x)
    
d = test()
d.print_num()
d.print_num = 'g'
print(d.print_num)

class Animal: #polymorphism
  def type(self): 
    print("Various types of animals")
      
  def age(self): 
    print("Age of the animal.") 
    
class Rabbit(Animal): 
  def age(self): 
    print("Age of rabbit.")

a = Animal()
r = Rabbit()
print(r.type())
print(r.age())

class dunder():

    def __len__(self):
        print('replacement')

print('ffgf'.__len__())

x = dunder()
print(x.__len__())

from functools import reduce
arr = [1,2,3]

def accumulator(acc, item): #acc is transient and continuously becomes acc + item
    return acc + item

print(reduce(accumulator, arr, 0)) #arguments: function, iterable, initial accumulator


#an example of a decorator to superboost a a function
from time import time
def preformance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'took {t2-t1}s')
    return wrapper

@preformance
def hihi():
    print('hi')

def args_test(*args, **kwargs):
    print(args,kwargs)
    
#error handling test
def error_test(arr):
    try:
        print(int(arr[0]))
    except (IndexError, ValueError):
        print('error')
    else:
        print('all good')

#generator test
def generator(arr):
    for i in range(len(arr)):
        try:
            yield i
        except:
            return
        
#debugger test
import pdb

def add(num1,num2):
    pdb.set_trace()
    t = 1+1
    return num1 + num2

# Removes the codeblock when pasting from other websites
def cleanup_code(content):
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

#testing asynchronous programming
import asyncio
anim = None
def hi():
    print('hi')
    return

async def hello():
    print('hello')


hi()
asyncio.run(hello())


