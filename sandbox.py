#Author: Terry Su
#Date: June 17, 2021
#Purpose: a coding sandbox to test out algorithms or datastructures

def reverse(s):
    
    if s == '':
        return ''
    
    return s[-1] + reverse(s[:-1])

def reverse2(s):
    return s[::-1]

def bubble_sort(arr):
    
    count = len(arr) - 1
    
    while count != 0:
        
        for i in range(0,count):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]

        count -= 1

    return arr

def selection_sort(arr):

    count = 0

    while count < len(arr):

        min_val = arr[count]

        for i in range(count,len(arr)):
            min_val = min(arr[i],min_val)

        min_index = arr.index(min_val)
        arr[count], arr[min_index] = arr[min_index],arr[count]

        count += 1

    return arr

def insertion_sort(arr):

    for i in range(1,len(arr)):

        curr = arr[i]

        for j in range(0,i):
            if curr <= arr[j]:
                arr.insert(j,curr)
                arr.pop(i+1)
                break
                
    return arr
