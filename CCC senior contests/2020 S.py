#Name: Terry Su
#Date: April 14, 2021
#Purpose: CCC 2020 senior questions

#Q1
N = int(input())

data = [input().split() for x in range(0,N)]
data = sorted(data, key = lambda time_speed: time_speed[0])

speeds = []

for x in range(0,len(data)-1):
    speeds.append((int(data[x+1][1]) - int(data[x][1])) / (int(data[x+1][0]) - int(data[x][0])))

for i,x in enumerate(speeds):
    if x < 0:
        speeds[i] = x * -1

print(max(speeds))

#Q2 (exceeded time limit for last subtask but correct algorithm)
    
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

#Q3 (exceeded time limit for subtasks 2-4 but correct algorithm)

N = input()
H = input()

N_vars = []
ans = 0

def permute(curr, remaining): #find all permutations first through recursion

    def remove(i, s):
        return s[:i] + s[i+1:]

    global N_vars
    
    if remaining == '':
        if curr not in N_vars:
            N_vars.append(curr)

    else:
        for index,char in enumerate(remaining):
            chars_left = remove(index, remaining)
            permute(curr+char, chars_left)

permute('',N)

for needle in N_vars: #try and find each permutation of the needle
    if H.find(needle) != -1:
        ans += 1

print(ans)
