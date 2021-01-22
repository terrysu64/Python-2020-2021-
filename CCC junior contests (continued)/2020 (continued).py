#Name: Terry Su
#Date: July 16, 2020
#Purpose: CCC 2020 junior questions

#Q1
print('Q1')
small = int(input('enter the number of SMALL treats Barley received: '))
while small < 0 or small >= 10:
    print('your input was not valid, try again.')
    small = int(input('enter the number of SMALL treats Barley received: '))
    
medium = int(input('enter the number of MEDIUM treats Barley received: '))
while medium < 0 or medium >= 10:
    print('your input was not valid, try again.')
    medium = int(input('enter the number of MEDIUM treats Barley received: '))
    
large = int(input('enter the number of LARGE treats Barley received: '))
while large < 0 or large >= 10:
    print('your input was not valid, try again.')
    large = int(input('enter the number of LARGE treats Barley received: '))

print()
total = small + (2 * medium) + (3 * large)
if total >= 10:
    print('happy')
else:
    print('sad')
print()

#Q2
print('Q2')
P = int(input('what is the total of infected people you want to calculate: '))
N = int(input('how many people have the disease currently: '))
R = int(input('how many others does each infected person infect daily: '))
day = 0
next_group = N
while N <= P:
    N += (next_group * R)
    next_group *= R
    day += 1
print(day)
print()

#Date: January 21, 2020
#Q3
print('Q3')
coor_x = []
coor_y = []

N = int(input())

for x in range(0,N):
    coordinates = input()

    comma = coordinates.find(',')
    
    coor_x.append(float(coordinates[0:comma]))
    coor_y.append(float(coordinates[comma + 1: len(coordinates) + 1]))

min_x = 1000
min_y = 1000
max_x = -1000
max_y = -1000

for x in coor_x:

    if x > max_x:
        max_x = x

    if x < min_x:
        min_x = x

for y in coor_y:

    if y > max_y:
        max_y = y

    if y < min_y:
        min_y = y

print(str(int(min_x)-1) + ',' + str(int(min_y)-1))
print(str(int(max_x)+1) + ',' + str(int(max_y)+1))

#Q4
text = input()
c = input()

ans = 0

if text.find(c) != -1:
        ans += 1

for x in range(0, len(c)):
    c += c[0:1]
    c = c.replace(c[0:1], '', 1)

    if text.find(c) != -1:
        ans += 1

if ans == 0:
    print('no')

else:
    print('yes')

    
    


    
    
    
