#Name: Terry Su
#Date: March 18, 2021
#Purpose: CCC 2021 senior questions

#Q1
fences = int(input())
heights= [int(x) for x in input().split(' ')]
widths = [int(x) for x in input().split(' ')]

area = 0

for x in range(0,fences):
    area += ((heights[x] + heights[x+1]) / 2) * widths[x]

print(area)

#Q2(exceeded time limit for last subtask but correct algorithm)
row = int(input())
column = int(input())

grid = []
for x in range(0,row):
        grid.append(['B' for r in range(0,column)])


brushes = []

brush = int(input())
for x in range(0,brush):
    b = input()
    brushes.append(b)


#solve
for stroke in brushes:
    direction = stroke[0:1]
    specif = int(stroke[2:]) - 1

    if direction == 'R':
        for index,color in enumerate(grid[specif]):
            if color == 'B':
                grid[specif][index] = 'G'
            else:
                grid[specif][index] = 'B'

    else:
        for x in range(0,row):
            if grid[x][specif] == 'B':
                grid[x][specif] = 'G'

            elif grid[x][specif] == 'G':
                grid[x][specif] = 'B'
       
count = 0
for x in grid:
    for y in x:
       if y == 'G':
           count += 1

print(count)

#Q3 (exceeded time limit for 3 subtasks but correct algorithm)

N = int(input())
stats = []
times = []
max_pos = 0
min_pos = 1000000 

for x in range(0,N):
    
    stat = input()
    stats.append(stat.split())
    
    max_pos = max(max_pos, int(stat.split()[0]))
    min_pos = min(min_pos, int(stat.split()[0]))

def calc_time(c):
    global times
    global stats

    time = 0

    for friend in stats:
        
        friend[0] = int(friend[0])
        friend[1] = int(friend[1])
        friend[2] = int(friend[2])
        
        if friend[0] > c:
            if friend[0] - c > friend[2]:
                time += (friend[0] - c - friend[2]) * friend[1]

        elif friend[0] < c:
            if c - friend[0] > friend[2]:
                time += (c - friend[0] - friend[2]) * friend[1]

    times.append(time)
        

    
if max_pos == min_pos:
    print(0)

else:
    for c in range(min_pos, max_pos + 1):
        calc_time(c)
        
    print(min(times))
