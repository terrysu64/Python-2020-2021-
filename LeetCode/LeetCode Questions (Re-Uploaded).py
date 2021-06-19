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
    #'4321')

#Date: January 12, 2021

#Given n pairs of parentheses, write a function to
#generate all combinations of well-formed parentheses.

def generateParenthesis(n):
    #choices: ( or )
    #constraints: must start with ( and end with )
    #goal: to end up generateing with ocount and ccount == 0 (no more characters to use)

    res = []
        
    def inner(curr,l,r):
    #curr is the current state of the 'possibility' we are working on
    #l is number of '(' we have left
    #r is number of ')' we have left
            
        # if current string hit n*2 then stop (the 'possibility' has been completed)
        
        if len(curr) == n*2:
            res.append(curr)
            return
            
        #branching out curr with left parens added until no more remaining
        
        if l>0:
            inner(curr+"(", l-1, r)
                
        #branching curr with right parens added if a left matches it and there are remaining
            
        if r>0 and r>l: #second condition is if the number of ( placed > number of ) placed
            inner(curr+")", l, r-1)
                    
    inner("",n,n)
    return res

#Date: Feburary 28, 2021

#Given an integer x, return true if x is palindrome integer.
#An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

def isPalindrome(x):
    x = str(x)
    reverse = x[-1::-1] #use slice notation to reverse input; start from index -1 and step backwards by one at a time till the start

    if x == reverse:
        return True

    else:
        return False
    
#Date: March 4, 2021

#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:

#1.Open brackets must be closed by the same type of brackets.
#2.Open brackets must be closed in the correct order.

def isValid(s):
    #strategy: remove all the  () [] and {}, if theres still something left after, then its false

    while True:
        
        first = s.find('()')

        if first != -1:
            s = s.replace(s[first:first+2], '', 1)

        second = s.find('[]')

        if second != -1:
            s = s.replace(s[second:second+2], '', 1)

        third = s.find('{}')

        if third != -1:
            s = s.replace(s[third:third+2], '', 1)

        if first == -1 and second == -1 and third == -1:
            break

        print(s)

    if len(s) == 0:
        return True

    else: 
        return False
    
#Alternative through stacking: check for 'first in first out' (better time complexity)

def isValid2(s):
    dic = {'(':')', '[':']', '{':'}'}
    current = []

    for y in range(0,len(s)): #scan each character of the string at a time
        
        if s[y:y+1] in dic: #if its an open bracket add it to array
            current.append(s[y:y+1])

        else: #if its a closed bracket

            if len(current) == 0: #if it matches nothing at all, string is invalid
                return False

            elif s[y:y+1] == dic[current[-1]]: #if it matches most recent open bracket
                current.pop()

            else: #if it doesnt match most recent open bracket, string is invalid
                return False

    if len(current) == 0:
        return True

#Date: March 6, 2021

#Given an array 'nums' and a value 'val',
#remove all instances of that value in-place and return the new length.
        
def removeElement(nums,val):
    
    while nums.count(val) != 0: #track how many elements in nums still = val
        nums.remove(val) #remove the elements that = val

    return len(nums)

#Date: March 6, 2020

#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

def rotate(matrix):
    #append the new version entirely to the tail of the original. Then remove the original
    leng = len(matrix) 
    current = []
    count = 0
    
    for x in range(0,leng):
        
        for y in range(1,leng + 1):
            current.append(matrix[(y+count) * -1][x]) #its y + count because there will be new parts of the new matrix(final objective) tailgating the original one

        count += 1

        matrix.append(current)
        current = []

    for x in range(0,leng):
        matrix.pop(0)

    return

#Date: March 8, 2021

#Given a string s, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(s):

    #use sliding window/2 pointer method
    
    longest = 0
    start = 0
    seen = {}

    for end, char in enumerate(s): #END pointer consistently moves forward by 1 index at a time

        if char in seen and seen[char] >= start: #if character has been seen AND has its last occurence in front of the START pointer, 
            start = seen[char] + 1               #then move START pointer to one index in front of it

        seen[char] = end #continue updating characters and most recent index
        longest = max(longest, end - start + 1) #continue compare current longest substring length with pointer distance

    return longest

#Date: March 14, 2021

#Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

def findMedianSortedArrays(nums1,nums2):
    #join the two arrays together then keep removing min and max values till we acheive the median

    nums1 += nums2

    while len(nums1) > 2:
        nums1.remove(max(nums1))
        nums1.remove(min(nums1))

    if len(nums1) == 1:
        return nums1[0]

    else:
        return (nums1[0] + nums1[1]) / 2

#Date: April 3, 2021
    
#Alternative solution: join and sort two lists, then use length of list to determine median (better time complexity)

def findMedianSortedArrays2(nums1,nums2):

    nums1 = sorted(nums1 + nums2)

    if len(nums1) % 2 == 0:
        return (nums1[(len(nums1) // 2) - 1] + nums1[(len(nums1) // 2)]) / 2

    else:
        return nums1[(len(nums1) // 2)]

#Date: April 11, 2021

#Given a string s, return the longest palindromic substring in s.

def longestPalindrome(s):
    #loop through the center of the possible palidrome (an index in s or two adjacent indices) and expand out.
    
    ans = ''

    for index in range(0,len(s)): #for each index, expand from the index AND from the index+next index (i.e something like expanding from "bb" for a palindrome "abba")
        
        curr = expand(s,index,index)
        if len(curr) > len(ans):
            ans = curr

        if index < len(s) - 1:
            curr = expand(s,index,index+1)
            
            if len(curr) > len(ans):
                ans = curr
                
    return ans

def expand(s,left,right): #function to call on, expands outwards from given index(s) while the substring is a valid palindrome

    curr = ''

    while left >= 0 and right < len(s) and s[left:right+1] == s[left:right+1][::-1]:

        if len(s[left:right+1]) > len(curr):
            curr = s[left:right+1]

        left -=1
        right += 1

    return curr

#Date: April 12, 2021
#Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

#The algorithm for myAtoi(string s) is as follows:

#1. Read in and ignore any leading whitespace.

#2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either.
#   This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.

#3. Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the string is ignored.

#4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
#   If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).

#5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
#   Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

#6. Return the integer as the final result.

def myAtoi(s):
    sign = True #sign value of integer (True = +ve, False = -ve)
    ints = ['0','1','2','3','4','5','6','7','8','9']
    start = 0
    end = 0
    count = 0
    
    s = s.strip() #1

    if s[0:1] == '-': #2
        sign = False
        s = s[1:]
        
    elif s[0:1] == '+':
            s = s[1:]


    while s[end:end+1] in ints: #3
        end += 1
    s = s[start:end]


    while s[count:count+1] == '0': #4,5
        count += 1
    s = s[count:]

    if s != '':
        s = int(s)

        if sign == False:
            s = s * -1

    else:
        s = 0

    if s > (2**31) - 1: #clamping s within range if out of range
        s = (2**31) - 1

    elif s < -1 * (2**31):
        s = -1 * (2**31)

    return s #6

#Date: April 16, 2021
#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".

def longestCommonPrefix(strs):
    #compare prefixes through checking one character at a time
    
    longest = ''
    count = 1
        
    if strs == [] or '' in strs:
        return ''            
        
    else:
        while all(sub[:count] == strs[0][:count] for sub in strs) == True and count <= min([len(s) for s in strs]): #stop checking when prefix stops matching
            count += 1                                                                                              #or when length of shortest string is exceeded

        return strs[0][:count-1]

#Date: May 2, 2021
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#Return the answer in any order.
    
def letterCombinations(digits):
    if digits == '': return [] #if we receive empty string
        
    maps = {             #construct hash table to link digits to respective characters
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
    
    res = []
    
    def build(curr, count): #for each digit (in order) branch out all possibilities using an initial for loop
                            #use recursion to add on sequential possibilities (characters associated with 'next' digit)
                            #and stop/append answers once we've reached end of digit sequence.
            
        if count == len(digits):
                res.append(curr)
            
        else:
            for char in maps[digits[count]]:
                build(curr+char,count+1)
            
                        
    for char in maps[digits[0]]:
            build(char,1)
                  
    return res

#Date: May 7, 2021
#Given an array of integers nums sorted in ascending order, find the starting and ending position (inclusive) of a given target value.
#If target is not found in the array, return [-1, -1].

def searchRange(nums,target):
    try:
        start = nums.index(target) #aquire starting index of target
            
    except ValueError: #if the target doesnt exist (question solved)**
        return [-1,-1]
        
    end = start #set default ending index to be equal to start
    curr = target
        
    while curr == target: #Increment index by one and stop when the value in the array no longer = the target
            
        end += 1
            
        try:
            curr = nums[end]
            
        except IndexError: #if the array ends, then break the loop as well
            break
        
    return [start, end-1] #because we increment, THEN CHECK, the final end value will be one more than expected

#Date: May 25, 2021: (not done)
#Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

def longestValidParentheses(s):
    #use stack where we always have a BASE INDEX (could be at [0] or higher) and acts as index of most recent '(' - 1 or index of ')' that rendered the current sub-parenthesis' invalid and acts as new start
    #(except for initial state of -1)
        
    #when theres '(' we push the index onto the stack, 
    #and when it gets matched we:
        # 1. pop the '(' index it matches with
        # 2. find max valid current sub-parenthesis' length by doing current index - base index
        
    #we can encouter 2 issues that render the sub-parenthesis' invalid:
        # a. more ')' than '('
            #solution: since after the pop() the stack will be empty, we simply ignore 2. and set the ')' index as new BASE INDEX
        # b. extra '('s that arent getting matched
            #solution: BASE INDEX is automatically shifted to match most recent '(' when we append the indexs of '('

            
    stack = [-1]    
    res = 0
        
    for index,curr in enumerate(s):
            
        if curr == '(':
            stack.append(index)
            
        elif curr == ')':
                
            stack.pop()
                
            try:
                res = max(res, index - stack[-1]) #by doing index - stack[-1] we match ')' with most recent '(' and protect against cases like ()(()
                
            except IndexError: #when stack is empty, AKA: theres more ')' than '('
                stack.append(index)
        
    return res

#Date: May 27, 2021 
#Given an array of distinct integers candidates and a target integer target,
#return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

#The same number may be chosen from candidates an unlimited number of times.
#Two combinations are unique if the frequency of at least one of the chosen numbers is different.

#It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

def combinationSum(candidates,target):

    #a recursive method to branch out all possibilities and only keeping those who add up to target

    res = []
        
    def scan(ans,target):
            
        if target == 0:
            if sorted(ans) not in res:
                res.append(sorted(ans))
            return
            
        elif target < 0:
            return
            
        for num in candidates: #looping over every candidate and substract from how far we are to acheiving the target
                                                #we keep track of used candidates, and how far we are from current value
            scan(ans+[num],target-num)
        
    scan([],target)

    return res

#Date: May 30, 2021 
#Write a program to solve a Sudoku puzzle by filling the empty cells.
#**each cell is filled with a string

#A sudoku solution must satisfy all of the following rules:
#Each of the digits 1-9 must occur exactly once in each row.
#Each of the digits 1-9 must occur exactly once in each column.
#Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#The '.' character indicates empty cells.

def possible(board,value,r,c): #r = row, c = column

    box_coor = [[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)], #box coordinates by row
                [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],
                [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],
                [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],
                [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],
                [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],
                [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],
                [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],
                [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]]
        
    #check row
    if value in board[r]:
        return False

    #check column
    if value in [x[c] for x in board]:
        return False

    #check box
    for box in box_coor:
        if (r,c) in box:
            if value in [board[spot[0]][spot[1]] for spot in box]:
                return False
        
    return True

#a backtracking method was used through recursion to step through one cell at a time
#each cell = a deeper layer of the recursive function

def solveSudoku_allAns(board):
    empty = 0 #return answer if no empty cells are left
    for r in board:
        for c in r:
            if c == '.':
                empty += 1
    if empty == 0:
        ans += 1
        return print(board)

    r,c = None,None
            
    for r_index, r_value in enumerate(board): #aquire empty cell coordinates (row and column indices)
        if '.' in r_value:
            r,c = r_index, r_value.index('.')
            break
            
    if r != None:
        for num in range(1,10): #try each number in empty cell
                            
            pos = possible(board,str(num),r,c)

            if pos == True:
                board[r][c] = str(num)
                solveSudoku(board) #if the number is possible, push it through the recursive function and proceed to next cell
                board[r][c] = '.'
               
ans = 0
def solveSudoku_oneAns(board):

    global ans

    if ans == 0:
        
        empty = 0
        for r in board:
            for c in r:
                if c == '.':
                    empty += 1
        if empty == 0:
            ans += 1
            return print(board)

        r,c = None,None
            
        for r_index, r_value in enumerate(board):
            if '.' in r_value:
                r,c = r_index, r_value.index('.')
                break
            
        if r != None:
            for num in range(1,10):
                            
                pos = possible(board,str(num),r,c)

                if pos == True:
                    board[r][c] = str(num)
                    solveSudoku(board)
                    board[r][c] = '.'

    else:
        return

#Date: June 3, 2021 
#Given a collection of candidate numbers (candidates) and a target number (target),
#find all unique combinations in candidates where the candidate numbers sum to target.

#Each number in candidates may only be used once in the combination.
#Note: The solution set must not contain duplicate combinations.

def combinationSum2(candidates,target):
        
    res = []
        
    def push(used,left,needed,count): #needed is value needed to acheive target
        if needed < 0:
            return
            
        elif needed == 0:
            if sorted(used) not in res:
                res.append(sorted(used))
            return
        
        else:
            for index,value in enumerate(left):
                push(used+[value],[j for i,j in enumerate(left) if i != index],needed-value,count+1)
        
    push([],candidates,target,0)
       
    return res


#Date: June 10, 2021
#You are given two non-empty linked lists representing two non-negative integers.
#The digits are stored in REVERSE order, and each of their nodes contains a single digit. 
#Add the two numbers and return the sum as a linked list.

#You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def convert(arr): #convert array to Linked List (most likely built in the LeetCode problem in the back-end)
    if arr[0]:
        res = ListNode()
        
        for index,element in enumerate(arr): #we can use a SHALLOW COPY variable to traverse the linked list and append each digit
            curr = res
            while curr.next:
                curr = curr.next
            curr.val = element

            if index != len(arr) - 1: #exception for last value in array (we dont want an extra empty node)
                curr.next = ListNode()

    return res
            
def addTwoNumbers(l1,l2): 

    l1,l2 = map(convert,[l1,l2])
    
    curr1,curr2 = l1,l2
    val1 = []
    val2 = []
        
        
    while curr1 != None: #reverse digits in linked lists and store as array
            
        val1.insert(0, str(curr1.val))
        curr1 = curr1.next
        
    while curr2 != None:
            
        val2.insert(0, str(curr2.val))
        curr2 = curr2.next
        

    target = [int(x) for x in list(str(int(''.join(val1)) + int(''.join(val2))))] #add two integers once reversed
    target.reverse() #reverse the result 
        
    res = convert(target)

    return res

#alternate solution (better time + memory complexity):
#sorta like doing (sorta like 123
                            # 345
                        #  +---------but from the opposite side

def addTwoNumbers2(l1,l2):

    l1,l2 = map(convert,[l1,l2])

    carry = 0
    res = n = ListNode(0) #n is shallow copy of res

    while l1 or l2 or carry: #checking if 'carry' exists is for the last digit's carryover
                 # 0 or None -> False in most languages
        if l1:
            carry += l1.val
            l1 = l1.next
                
        if l2:
            carry += l2.val #do the addition without the carryover digit first
            l2 = l2.next
            
        carry, val = divmod(carry, 10) #divmod returns quotient,remainder
        n.next = n = ListNode(val) #n is shallow copy of n.next so we can traverse the linked list
            
    return res.next

#Date: June 14, 2021
#Merge two sorted linked lists and return it as a sorted list.
#The list should be made by splicing together the nodes of the first two lists.

def mergeTwoLists(l1,l2):

    l1,l2 = map(convert,[l1,l2])

    if l1 == None and l2 == None:
        return
        
    curr1, curr2 = l1, l2
    conv = []
        
    while curr1: #all values in both linked-lists are appended to a single array
        conv.append(curr1.val) 
        curr1 = curr1.next
        
    while curr2:
        conv.append(curr2.val)
        curr2 = curr2.next
        
    conv.sort() #the array is sorted


    #the array is re-converted into a linked-list 
    ans = curr = ListNode()
    for i,x in enumerate(conv):
            
        curr.val = x
            
        if i != len(conv)-1:
            curr.next = curr = ListNode()
        
    return ans

#Date: June 16, 2021
#Given an unsorted integer array nums, find the smallest missing positive integer.
#You must implement an algorithm that runs in O(n) time

def firstMissingPositive(self, nums):
        
    store = set([i for i in nums])
    ans = 1
        
    while ans in store: #prevents O(n^2) as sets have lookup of O(1)
                        #a set is implemented as values in a hash table
        ans += 1
            
    return ans

#Date: June 17, 2021
#Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

#Symbol       Value

#I             1
#V             5
#X             10
#L             50
#C             100
#D             500
#M             1000
#For example, 2 is written as II in Roman numeral, just two one's added together.
#12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

#Roman numerals are usually written largest to smallest from left to right.
#However, the numeral for four is not IIII. Instead, the number four is written as IV.
#Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.
#There are six instances where subtraction is used:

#I can be placed before V (5) and X (10) to make 4 and 9. 
#X can be placed before L (50) and C (100) to make 40 and 90. 
#C can be placed before D (500) and M (1000) to make 400 and 900.
#Given a roman numeral, convert it to an integer.

def romanToInt(s):
    
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    ans = 0

    #Ideally, we can iterate through the string and sum up corresponding values to the symbols one by one
    #The only exception is in scenarios where there is a sub-string with the value of 4 * 10^x (x = 0 or xEZ+)
        #to solve this we can check if value of very next index > value at current index and substract value at current index if true
    
    for i in range(0, len(s) - 1):
            
        if roman[s[i]] < roman[s[i+1]]:
            ans -= roman[s[i]]
                
        else:
            ans += roman[s[i]]
                
    return ans + roman[s[-1]] #for the last index of string so we dont encounter IndexError

#Date: June 18, 2021
#Given a sorted array of distinct integers and a target value, return the index if the target is found.
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.

def searchInsert(nums,target):
    #use divide and conquer
    #Note: len(), and indexing have a time complexity of O(1)
        
    #special conditions:
    if len(nums) == 0: #nums is empty
        return 0
        
    if len(nums) == 1: #nums only has one value
        if target <= nums[0]:
                return 0
            
        elif target > nums[0]:
            return 1
        
    if target > nums[-1]: #target is larger than everything
        return len(nums)
        
    if target < nums[0]: #target is smaller than everything
        return 0
        
        
    def divide(curr):
        #1. break the array to left and right
        #2. check if target if on edges of left and right, or recurse by splitting either left or right into a smaller arrays (depending on the situation)
            
        left, right = curr[:len(curr)//2], curr[len(curr)//2:]
        left_compare, right_compare = left[-1], right[0]
            
        if target == left_compare: #target found!
            return nums.index(left_compare)
                
        elif target == right_compare: #target found!
            return nums.index(right_compare)
                
        elif target > right_compare: #target in right sub-array somewhere
            return divide(right)
                    
        elif target < left_compare: #target in left sub-array somewheere
                return divide(left)

        else: #target doesnt exist
            return nums.index(left_compare) + 1
        
    return divide(nums)

#Date: June 19, 2021
#Given the head of a linked list, REMOVE the nth node from the end of the list and return its head.

def removeNthFromEnd(head):

    curr = head
    length = len_linked_list(head) #find length of linked list first

    #special conditions
    if head == None or head.next == None: #if linked list is empty or only has one node
        return
        
    if n == length: #if the first node needs to be removed
        return head.next
        
    for x in range(0,length-n-1): #find node before the nth node from end; we need to add the -1 as we start initially on the head node as we traverse
        curr = curr.next
        
    curr.next = curr.next.next #this resets the sucessor of the node BEFORE the removed node to the node initially AFTER the removed node
    return head
    
def len_linked_list(linked_list = None):
        
    count = 0
    curr = linked_list
        
    while curr:
        curr = curr.next
        count += 1
        
    return count
