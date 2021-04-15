#Author: Terry Su
#Purpose: some useful notes and tips

#THE ALL() & ANY() FUNCTION

#The all() function returns True if all items in an iterable are true, otherwise it returns False.
#If the iterable object is empty, the all() function also returns True.

#Params:
#the iterable

#Note: When used on a dictionary, the all() function checks if all the keys are true, not the values.

#Examples:
x = [1,2,0]
print(all(x))

#conditions can also be used where
#all(condition(item) for item in iterable)

print(all(element < 5 for element in x))

#The any() function returns True if at least one item in an iterable are true, otherwise it returns False.

print(any(x))
print(any(element == 0 for element in x), '\n')






#THE ZIP() FUNCTION

#The zip() function returns a zip object, which is an iterator of tuples where the items of each iterator passed for respective indexes are paired together
#***assuming all iterators have a value at that index

#Syntax:
#zip(iterator1, iterator2, iterator3 ...)

#Params:
#the iterables to zip


#Examples:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = [1,2,3]

x = zip(a, b, c)
print(tuple(x), '\n') #use the tuple() function to display a readable version of the result





#THE .GET() FUNCTION

#The get() method returns the value of the item with the specified key.
#get() method takes maximum of two parameters:

#Syntax:
#dictionary.get(keyname, value)

#Params:
#key - key to be searched in a dictionary
#value (optional) - Value to be returned if the key is NOT found, would return None if not specified

#Examples:
dic = {'a':'b'}
print(dic.get('a'))
print(dic.get('f'))
print(dic.get('sdsdsd','cant find'), '\n')





#THE .SPLIT() FUNCTION ***useful for CCC inputs

#The split() method splits a string into a list.
#You can specify the separator, default separator is any whitespace.

#Syntax:
#string.split(separator, maxsplit)

#Params:
#separator (optional) - Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit (optional) -  Specifies how many splits to do. Default value is -1, which is "all occurrences"

#Examples:
txt = 'i am terry'
print(txt.split())
print(txt.split(' ', 1), '\n')





#THE .INSERT() FUNCTION

#The .insert() method inserts a certain value into a specific index of an array
#all indices after that index are shifted down by one

#Syntax:
#list.insert(index, value)

#Params:
#index - which index your want to insert in
#value - what is the value you want to insert

#Example
x = ['a','b','c','d']
x.insert(2, 'hi') #c and d are shifted down by one index
print(x, '\n')





#THE .JOIN() FUNCTION

#The .join() The method takes all items in an iterable and joins them into one string.
#A string must be specified as the SEPERATOR.

#Syntax:
#string.join(iterable)

#Params:
#iterable - Any iterable object where all the returned values are strings

#Example
x = ''
a = ['a','b','c']
print(x.join(a))
print(' '.join(a), '\n')





#THE SORTED() FUNCTION

#The sorted() function returns a sorted list of the specified iterable object.
#You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

#Syntax:
#sorted(iterable, key=key, reverse=reverse)

#Params:
#iterable - The sequence to sort, list, dictionary, tuple etc.
#key (Optional) - A Function to execute to decide the order. Default is None
#reverse(Optional) - A Boolean. False will sort ascending, True will sort descending. Default is False

#sorted(iterable, key=key, reverse=reverse)

#Examples:
l = ['a','g','b']
print(sorted(l))
x = [1,3,5,2,5]
print(sorted(x), '\n')





#THE MAP() FUNCTION

#The map() function executes a specified function for each item in an iterable.
#The item is sent to the function as a parameter.

#Syntax:
#map(function, iterables)

#Params:
#function - The function to execute for each item
#iterables - A sequence, collection or an iterator object.
#            You can send as many iterables as you like, just make sure the function has one parameter for each iterable.

#Examples:
def length(element):
    return len(element)

output = list(map(length, ['dd','ggg','dffgg'])) #convert to list for readability
print(output)

output = list(map(lambda x,y: x + y, [1,2,3,4],[2,3,4,5]))
print(output, '\n')
