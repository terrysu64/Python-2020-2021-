#Name: Terry Su
#Date: Dec 28, 2020
#Purpose: Python questions taken from LeetCode to try during the winter break

#Q.1  You are given two non-empty lists representing two non-negative integers.
#     The digits are stored in reverse order, and each of their nodes contains a single digit.
#     Add the two numbers and return the sum as a list. There are no leading zeros

def solution1(L1i,L2i):
    #making list not reversed
    L1 = []
    L2 = []
    Lsum = []
    Lsum2 = []
    Lfinal = []
    
    string = ''
    count = 1
    count2 = 0
    
    while count <= len(L1i):
        L1.append(L1i[len(L1i) - count])
        count += 1

    count = 1
    
    while count <= len(L2i):
        L2.append(L2i[len(L2i) - count])
        count += 1
    
    #adding two new lists together (without bringing over the 1s, and reverse)
    count = len(L1) - 1
    count2 = len(L2) - 1

    while count >= 0 and count2 >= 0:
        Lsum.append(L1[count] + L2[count2])
        count -= 1
        count2 -= 1

    if count > count2:
        while count >= 0:
            Lsum.append(L1[count])
            count -= 1
            
    elif count2 > count:
        while count2 >= 0:
            Lsum.append(L2[count2])
            count2 -= 1

    #unreversing
    for x in range(len(Lsum)):
        Lsum2.append(Lsum[len(Lsum) - 1 - x])


    #bringing over 1s 
    for x in range(len(Lsum2) - 1):
        if Lsum2[len(Lsum2) - 1 - x] > 9:
                Lsum2[len(Lsum2) - 1 - x] -= 10
                Lsum2[len(Lsum2) - 2 - x] += 1

    print(Lsum2)

    #finalizing
    if len(str(Lsum2[0])) > 1:
        Lfinal.append(1)
        Lfinal.append(Lsum2[0] - 10)
        for y in range(1,len(Lsum2)):
            Lfinal.append(Lsum2[y])
        print(Lfinal)

    else:
        print(Lsum2)

#Date: December 29,2020
#Q2. find the average(float) from 2 given arrays

def solution2(L1,L2):
    #move everything to one list
    for x in L2:
        L1.append(x)

    #total up everything in L1
    total = 0
    for x in L1:
        total += x

    #find average
    print(total / len(L1))

#Date: December 31, 2020       
#Q3 Convert an integer to Roman numerals. Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#Symbol       Value
#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000

def solution3(integer):
    #setting up all counters before iteration
    Numeral_count = [0,0,0,0,0,0,0]
    Divisors = [1000,500,100,50,10,5,1]

    #interating over each roman value at a time in the integer and appending how many there are to the Numeral_count list
    for index,div in enumerate(Divisors):
        Numeral_count[index] += integer // div
        integer -= (integer // div) * div

    Roman_values = ['M','D','C','L','X','V','I']
    Value = ''

    #converting to a proper roman numeral
    for x in range(0,7):
        Value += Numeral_count[x] * Roman_values[x]

    print(Value)
    
#Date: January 1, 2021
#Q4 Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#1. Each row must contain the digits 1-9 without repetition.
#2. Each column must contain the digits 1-9 without repetition.
#3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

def solution4(board):

    false_count = 0

    #check rows
    for row in board:
        
        for index1, element in enumerate(row):
            
            for index2, other in enumerate(row):
                if element == other and index1 != index2 and element != '.':
                    false_count += 1

    #check columns
    column_list = []
    
    for x in range(0,9):
        
        for column in range(0,9):
            column_list.append(board[column][x])
            
        for index1, element in enumerate(column_list):
            
            for index2, other in enumerate(column_list):
                if element == other and index1 != index2 and element != '.':
                    false_count += 1
            column_list = [] 

    #check each box

    box_list = []
        
    #first column of boxes
    for box_num in [0,3,6]:
        
        for x in range(box_num, box_num + 3):
        
            for y in range(0,3):
                box_list.append(board[x][y])

        for index1, element in enumerate(box_list):
            
            for index2, other in enumerate(box_list):
                if element == other and index1 != index2 and element != '.':
                    false_count += 1

        box_list = []

    #second column of boxes
    for box_num in [0,3,6]:
        
        for x in range(box_num, box_num + 3):
        
            for y in range(3,6):
                box_list.append(board[x][y])
        

        for index1, element in enumerate(box_list):
            
            for index2, other in enumerate(box_list):
                if element == other and index1 != index2 and element != '.':
                    false_count += 1

        box_list = []

    #third column of boxes
    for box_num in [0,3,6]:
        
        for x in range(box_num, box_num + 3):
        
            for y in range(6,9):
                box_list.append(board[x][y])
        

        for index1, element in enumerate(box_list):
            
            for index2, other in enumerate(box_list):
                if element == other and index1 != index2 and element != '.':
                    false_count += 1

        box_list = []
    

    if false_count > 0:
        print('False')

    else:
        print('True')
        
    
    
