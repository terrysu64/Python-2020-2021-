#Name: Terry Su
#Date: August 19, 2020
#Purpose: CCC 2018 junior questions

#Q1
print('Q1')
fourth = input()
third = input()
second = input()
last = input()

if (fourth=='8' or fourth =='9') and third==second and (last=='8' or last=='9'):
  print('ignore')
else:
  print('answer')
print()

#Q2
print('Q2')
N = int(input('How many parking spaces are there: '))
yesterday = input('Which ones were parked at yesterday: ')
today = input('Which ones were parked at today: ')

common = 0
count = 0
yesterdayL = []
todayL = []

for x in range(0, N):
    yesterdayL.append(yesterday[count:count + 1])
    todayL.append(today[count:count + 1])
    count += 1

for x in range(0,N):
    if yesterdayL[x] == todayL[x] and yesterdayL[x] == 'C':
        common += 1

print(common)
print()

#Q3
print('Q3')
city = input('Enter city distances: ')
copy = []
distance = []
num = ''
count = 0

for x in range(0,len(city)):
    copy.append(city[count:count + 1])
    count += 1

count = 0
for x in copy:
    if x == ' ':
        distance.append(num)
        num = ''
    else:
        num += x
distance.append(num)
print(distance)

d1 = int(distance[0])
d2 = int(distance[1])
d3 = int(distance[2])
d4 = int(distance[3])

print(0,d1,d1+d2,d1+d2+d3,d1+d2+d3+d4)
print(d1,0,d2,d2+d3,d2+d3+d4)
print(d1+d2,d2,0,d3,d3+d4)
print(d1+d2+d3,d2+d3,d3,0,d4)
print(d1+d2+d3+d4,d2+d3+d4,d3+d4,d4,0)

#Date: January 23, 2021
#Q4

N = int(input())

grid = []
grid2 = []
grid3 = []
grid4 = []
grid_test = []
row = []
string = ''

#initializing grid

for x in range(0,N):
    row_input = input()

    for y in range(0,N - 1):
        
        num = row_input.find(' ')
        
        row.append(int(row_input[0:num]))
        row_input = row_input.replace(row_input[0:num+1], '', 1)
  

    row.append(int(row_input))
    grid.append(row)
    row = []

error = 0

#CHECKING ORIGINAL
#Checking original (rows)

for g in range(0,N):
    if not (all(i < j for i, j in zip(grid[g], grid[g][1:]))): #sorted in increasing order?
        error += 1
        break

#checking original (columns)
if error == 0:
    
    for f in range(0,N):
        for h in range(0,N):
            grid_test.append(grid[h][f])

        if not (all(i < j for i, j in zip(grid_test, grid_test[1:]))): #sorted in increasing order?
            error += 1
            break

        grid_test = []

#print grid if original is correct
if error == 0:
    for x in range(0,N):
        for y in range(0,N):
            string += str(grid[x][y]) + ' '
        print(string)
        string = ''

else:
    error = 0
    #CHECK 90 DEGREE
    for t in range(0,N):
        for u in range(0,N):
            row.append(grid[u][N - 1 - t])
        grid2.append(row)
        row = []

    #Checking (rows)

    for g in range(0,N):
        if not (all(i < j for i, j in zip(grid2[g], grid2[g][1:]))): #sorted in increasing order?
            error += 1
            break

    #checking (columns)
    if error == 0:
        
        for f in range(0,N):
            for h in range(0,N):
                grid_test.append(grid2[h][f])

            if not (all(i < j for i, j in zip(grid_test, grid_test[1:]))): #sorted in increasing order?
                error += 1
                break

            grid_test = []

    #print grid if it is correct
    if error == 0:
        for x in range(0,N):
            for y in range(0,N):
                string += str(grid2[x][y]) + ' '
            print(string)
            string = ''

    else:
        error = 0
        #CHECK 180 DEGREE
        for t in range(0,N):
            for u in range(0,N):
                row.append(grid2[u][N - 1 - t])
            grid3.append(row)
            row = []

        #Checking (rows)

        for g in range(0,N):
            if not (all(i < j for i, j in zip(grid3[g], grid3[g][1:]))): #sorted in increasing order?
                error += 1
                break

        #checking (columns)
        if error == 0:
            
            for f in range(0,N):
                for h in range(0,N):
                    grid_test.append(grid3[h][f])

                if not (all(i < j for i, j in zip(grid_test, grid_test[1:]))): #sorted in increasing order?
                    error += 1
                    break

                grid_test = []

        #print grid if it is correct
        if error == 0:
            for x in range(0,N):
                for y in range(0,N):
                    string += str(grid3[x][y]) + ' '
                print(string)
                string = ''

        else:
            #has to be 270 degrees if others dont work
            for t in range(0,N):
                for u in range(0,N):
                    row.append(grid3[u][N - 1 - t])
                grid4.append(row)
                row = []

            for x in range(0,N):
                for y in range(0,N):
                    string += str(grid4[x][y]) + ' '
                print(string)
                string = ''



        
    
    
    
