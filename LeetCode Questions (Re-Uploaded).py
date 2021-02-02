#Name: Terry Su
#Date: Dec 28, 2020
#Purpose: Python questions taken from LeetCode to try during the winter 2020-2021

#Date: Jan 7, 2021
#Valid Sudoku
#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:

#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self,board):

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
            return False

        else:
            return True

#Date: Jan 9, 2021
#Two sum
#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, and you may not use the same element twice.

#You can return the answer in any order.
        
def twoSum(nums,target):

    Lanswer = []

    #a simple iteration over the list to check for target sum
    for index1, integer1 in enumerate(nums):
        for index2, integer2, in enumerate(nums):

            if len(Lanswer) == 0 and integer1 + integer2 == target and index1 != index2:
                Lanswer.append(index1)
                Lanswer.append(index2)

    return Lanswer

#Date: Jan 9, 2021

#Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
#Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
        
def removeDuplicates(nums):

    #a simple iteration over the list to check for iterations
    ans = []
    for x in nums:
            
        if x not in ans:
            ans.append(x)

    return len(ans), ans

#Date January 11, 2021

#Given a 32-bit signed integer, reverse digits of an integer.

#Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
#For this problem, assume that your function returns 0 when the reversed integer overflows.

def reverse(x):

    #condition
    if x < -2 ** 31 or x > (2**31) - 1:
        return 0

    elif x == 0:
        return 0

    elif len(str(x)) == 1:
        return x

    #initialize

    store_p = []
    store_n = ['-']
    ans = ''

    #appending backwards into list as string and summing up
    #conversion to string then back to integer
    
    x = str(x)

    if int(x) > 0:
        for a in range(len(x)):
            store_p.append(x[len(x) - a - 1: len(x) - a])

        for y in store_p:
            ans += y
        ans = int(ans)

        return ans


    else:
        for a in range(len(x) - 1):
            store_n.append(x[len(x) - a - 1: len(x) - a])

        for y in store_n:
            ans += y
        ans = int(ans)

        return ans
    #a cool alternate function 'list[<start>:<stop>:<step>]'
    #(ex: a = '1234',
    #a[::-1]
    #('4321')

#Date: January 12, 2021

#Given n pairs of parentheses, write a function to
#generate all combinations of well-formed parentheses.

def generateParenthesis(n):
    #choices: ( or )
    #constraints: must start with ( and end with )
    #goal: to end up generateing with ocount and ccount == 0 (no more characters to use)

    res = []
        
    def inner(curr,l,r):
            
        # if current string hit n*2 then stop
        if len(curr) == n*2:
            res.append(curr)
            return
            
        # keep adding left parens until no more remaining
        if l>0:
            inner(curr+"(", l-1, r)
                
        # keep adding right parens if a left matches it
        # and there are remaining
        if r>0 and r>l:
            inner(curr+")", l, r-1)
                    
    inner("",n,n)
    return res
        

                

        

    
    
