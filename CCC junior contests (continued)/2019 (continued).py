#Name: Terry Su
#Date: July 29, 2020
#Purpose: CCC 2019 junior questions

#Q1
print('Q1')
apple3 = int(input('how many 3s did the apples score: '))
apple2 = int(input('how many 2s did the apples score: '))
apple1 = int(input('how many 1s did the apples score: '))
apple_total = (apple3 * 3) + (apple2 * 2) + apple1
print()

banana3 = int(input('how many 3s did the bananas score: '))
banana2 = int(input('how many 2s did the bananas score: '))
banana1 = int(input('how many 1s did the bananas score: '))
banana_total = (banana3 * 3) + (banana2 * 2) + banana1
print()

if apple_total > banana_total:
    print('A')
elif apple_total < banana_total:
    print('B')
else:
    print('T')
print()

#Q2
print('Q2')
L = int(input())

for x in range(0,L):
    
    current = input()

    num = current.find(' ')
    print(int(current[0:num]) * current[num+1: len(current) + 1])
print()
 
#Q3
print('Q3')
elements = []
L = int(input('enter the number of lines: '))

for x in range(0,L):
    elements.append(x)
for y in elements:
    elements[y] = input('enter message #' + str(y + 1) + ': ')
print()

for message in elements:
    copy_message = message
    output = ''
    for num in range(0,len(message)):
        length = len(copy_message)
        count = 0
        symbol = copy_message[0:1]
        while copy_message.find(symbol) >= 0 and symbol == copy_message[0:1] and symbol != '':
            count += 1
            copy_message = copy_message[1:length]
            length -= 1
        if count != 0:
            output += str(count) + ' ' +  symbol + ' '
    print(output)
print()

#Q4
print('Q4')
grid = [1,2,3,4]
flipsL = []
flips = input()

count = 0 
for x in range(0,len(flips)):
    flipsL.append(flips[count:count+1])
    count += 1

for x in flipsL:
    if x == 'H':
        grid0 = grid[2]
        grid1 = grid[3]
        grid2 = grid[0]
        grid3 = grid[1]

        grid[0] = grid0
        grid[1] = grid1
        grid[2] = grid2
        grid[3] = grid3
        
    elif x == 'V':
        grid0 = grid[1]
        grid1 = grid[0]
        grid2 = grid[3]
        grid3 = grid[2]

        grid[0] = grid0
        grid[1] = grid1
        grid[2] = grid2
        grid[3] = grid3

print(grid[0], grid[1])
print(grid[2], grid[3])
print()

#Date: Feburary 14, 2021
#Q5 (exceeded time limit for last subtask but correct algorithm)
import re

Rules = ['']

#Getting all rules and organizing
for x in range(0,3):
    Rule = input()
    Space = Rule.find(' ')

    Rules.append((Rule[0:Space],Rule[Space + 1:]))

#Getting desired result and organizingas list
Result = []

Result_input = input()
Space = Result_input.find(' ')

while Space != -1:
    Result.append(Result_input[0:Space])
    Result_input = Result_input.replace(Result_input[0:Space+1], '', 1)
    Space = Result_input.find(' ')

Result.append(Result_input)

#Solving note
#Solve though layer searching,
# for each layer(replacement made) all possible replacements are taken down temporarily them stored
#where each action is taken down as (string before, rule# used, index used + 1, string after)

#number of layers created besides layer of the original value = number of steps given in the input

All_Paths = []
Current_Layer = [['','','',Result[1]]]
Next_Layer = []

for x in range(0,int(Result[0])+1): #laying out possibilities of paths by layer#

    for String_Set in Current_Layer:
        
        String = String_Set[3]

        for Rule_Number in range(1,4):
            
            Sub = Rules[Rule_Number][0]
            Res = [i.start() for i in re.finditer(Sub, String)]

            for Index in Res:
                
                Next_Layer.append([String, Rule_Number, Index + 1, String[0:Index] + Rules[Rule_Number][1] + String[Index + len(Sub): ]])

    All_Paths.append(Current_Layer)
    Current_Layer = Next_Layer
    Next_Layer = []

#Backtracking to see which route the result took
#this is done through matching the  'string before' of the current layer
#with the 'string after' of the previous layer
    
Ans = []
Target = ''

for Final in All_Paths[int(Result[0])]:
    
    if Final[3] == Result[2]:
        Target = Final
        break  #if it is the answer or string we r looking for

Ans.append((Target[1],Target[2],Target[3]))

for x in range(2,int(Result[0]) + 1):

    for y in All_Paths[x * -1]:

        if y[3] == Target[0]:
            Target = y
            break
        
    Ans.append((Target[1],Target[2],Target[3]))

Ans.reverse() #reverse list

#output each individual step taken to reach result
for Answer in Ans:
    print(str(Answer[0]) + ' ' + str(Answer[1]) + ' '+ str(Answer[2]))
