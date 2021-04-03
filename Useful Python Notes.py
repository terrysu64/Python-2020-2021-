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
print(any(element == 0 for element in x))






#THE ZIP() FUNCTION

#The zip() function returns a zip object, which is an iterator of tuples where the items of each iterator passed for respective indexes are paired together
#assuming all iterators have a value at that index

#Params:
#zip(iterator1, iterator2, iterator3 ...)
#the iterables to zip


#Examples:
a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")
c = [1,2,3]

x = zip(a, b, c)
print(tuple(x)) #use the tuple() function to display a readable version of the result






#THE .GET() FUNCTION

#The get() method returns the value of the item with the specified key.
#get() method takes maximum of two parameters:

#Params:
#dictionary.get(keyname, value)
#key - key to be searched in a dictionary
#value (optional) - Value to be returned if the key is NOT found, would return None if not specified

#Examples:
dic = {'a':'b'}
print(dic.get('a'))
print(dic.get('f'))
print(dic.get('sdsdsd','cant find'))






#THE .SPLIT() FUNCTION ***useful for CCC inputs

#The split() method splits a string into a list.
#You can specify the separator, default separator is any whitespace.

#Params:
#string.split(separator, maxsplit)
#separator (optional) - Specifies the separator to use when splitting the string. By default any whitespace is a separator
#maxsplit (optional) -  Specifies how many splits to do. Default value is -1, which is "all occurrences"

#Examples:
txt = 'i am terry'
print(txt.split())
print(txt.split(' ', 1))




#THE .INSERT() FUNCTION

#The .insert() method inserts a certain value into a specific index of an array
#all indices after that index are shifted down by one

#Params:
#list.insert(index, value)
#index - which index your want to insert in
#value - what is the value you want to insert

#Example
x = ['a','b','c','d']
x.insert(2, 'hi')
print(x)

#THE .JOIN() FUNCTION

#The .join() The method takes all items in an iterable and joins them into one string.
#A string must be specified as the SEPERATOR.

#Params:
#string.join(iterable)
#iterable - Any iterable object where all the returned values are strings

#Example
x = ''
a = ['a','b','c']
print(x.join(a))
print(' '.join(a))

#THE SORTED() FUNCTION

#The sorted() function returns a sorted list of the specified iterable object.
#You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

#Params:
#sorted(iterable, key=key, reverse=reverse)
#iterable - The sequence to sort, list, dictionary, tuple etc.
#key (Optional) - A Function to execute to decide the order. Default is None
#reverse(Optional) - A Boolean. False will sort ascending, True will sort descending. Default is False

#sorted(iterable, key=key, reverse=reverse)

#Examples:
l = ['a','g','b']
print(sorted(l))
x = [1,3,5,2,5]
print(sorted(x))

