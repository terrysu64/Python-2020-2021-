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
