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
