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

#set up 2D array and change values according to each brush

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

#move the concert across each possible spot along the number line
#for each spot, calculate the total walking time of all friends together

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

def calc_time(c): #calculating total time for each position of concert
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
        
    print(min(times)) #return minimum total time

#Q4 (exceeded time limit for 3 subtasks but correct algorithm)

#N stations

#one train only that runs in station order S1,S2...SN (you want to get to N ASAP) represented by integers
#The order is not necessarily 1,2,3,4... tho
#train runs 1 min between stations

#Theres also walkways from station Ai to Bi (takes 1 min to get there)

#Route swaps Xith and Yith station everyday tho, ex: station order was [1,3,4]; X = 1, Y = 3 --> [4,3,1]

#find minimum time to get to Sn (school) everyday

#Collecting input
N_W_D = [int(x) for x in input().split()]

Walkways = {} #use hash table to match each station to array of stations you can get to though walkways
for x in range(0,N_W_D[1]):
    Curr = [int(x) for x in input().split()]
    
    if Curr[0] in Walkways:
        Walkways[Curr[0]].append(Curr[1])

    else:
        Walkways[Curr[0]] = [Curr[1]]


Station_Order = [int(x) for x in input().split()]

Daily_Swap = []
for x in range(0,N_W_D[2]):
    Daily_Swap.append([int(x)-1 for x in input().split()]) #indexes to swap instead of station #s


#Solving

def Day(Day_Number):
               
    global Station_Order #do the daily flip first
    Station_Order[Daily_Swap[Day_Number-1][0]], Station_Order[Daily_Swap[Day_Number-1][1]] = Station_Order[Daily_Swap[Day_Number-1][1]], Station_Order[Daily_Swap[Day_Number-1][0]]
    
    Times = [] #keeps track of all possible times to get to station N
    
    Max_Time = Station_Order.index(N_W_D[0]) #maximum time to get there would be a direct bus, once all route possbilities up to that time are calculated,
                                            #break the calculations 
    Times.append(Max_Time)

    def Branch(Time, Station): #Branching walkways through recursion
       
        for Next in Walkways[Station]: #if station N is reached, add to array of possible times
            if Next == N_W_D[0]:
                Times.append(Time+1)
               
            if Next in Walkways and Time < min(Times): #if a minimum time has been found, theres no point to compute further possibilities
                Branch(Time + 1, Next)                 #Otherwise, keep branching possibilities

    Time = 0
    for Curr in Station_Order: #At each station check if there are walkways, otherwise keep riding the train
        
        if Time >= min(Times): #if a minimum time has been found, theres no point to compute further possibilities
            break

        if Curr in Walkways:
            Branch(Time, Curr)

        Time += 1

    return(min(Times))

for x in range(1,N_W_D[2] + 1): #Calculations/answer for each day
    ans = Day(x)
    print(ans)

#Q5
