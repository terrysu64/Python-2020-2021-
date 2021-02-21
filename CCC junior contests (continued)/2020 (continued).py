#Name: Terry Su
#Date: July 16, 2020
#Purpose: CCC 2020 junior questions (full solutions)

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

#Date: January 22, 2021
#Q5 (exceeded time limit for last subtask but correct algorithm)
    
import math

M = int(input())
N = int(input())
grid = [[]]
row = []

#initializing grid

for x in range(0,M):
    row_input = input()
    row.append(' ')

    for y in range(0,N - 1):
        
        num = row_input.find(' ')
        
        row.append(int(row_input[0:num]))
        row_input = row_input.replace(row_input[0:num+1], '', 1)
  

    row.append(int(row_input))
    grid.append(row)
    row = []


#solving the question

ans = 0
use = 0

x = [1] #current factors or (R,C) being tested
y = [1]

x_copy = [] #all tested factors to reference for repitition
y_copy = [] 

current_number = grid[x[0]][y[0]] #current number will always be grid[x[0]][y[0]]

factor2 = 0


while len(x) > 0:

    for factor in range(1,(int(math.sqrt(current_number))) + 1):

        if current_number % factor == 0: # if it is a factor
            factor2 = current_number // factor 

            if factor <= M and factor2 <= N:   # if its in range of the grid

                for used in range(0, len(x_copy)):
                    if x_copy[used] == factor and y_copy[used] == factor2: #if it has been used
                        use += 1

                if use == 0:
                    x.append(factor)
                    x_copy.append(factor)

                    y.append(factor2)
                    y_copy.append(factor2)

                use = 0

            #now the opposite way where M and N are reversed

            if factor2 <= M and factor <= N:   # if its in range

                for used in range(0, len(x_copy)):
                    if x_copy[used] == factor2 and y_copy[used] == factor: #if it has been used
                        use += 1

                if use == 0:
                    x.append(factor2)
                    x_copy.append(factor2)

                    y.append(factor)
                    y_copy.append(factor)

                use = 0

    x.pop(0) #cut both lists by one to move on to next set of factors
    y.pop(0)

    if len(x) > 0: #check if its the current number
        current_number = grid[x[0]][y[0]]

        if x[0] == M and y[0] == N: #if it is add one to ans
            ans +=1
            break

if ans > 0:
    print('yes')

else:
    print('no')

    
    


    
    
    
