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

#Date: May 25, 2021:
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

#A DFS solution

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
                    solveSudoku_oneAns(board)
                    board[r][c] = '.'

    else:
        return

def solveSudoku_allAns(board):
    empty = 0
    for r in board:
        for c in r:
            if c == '.':
                empty += 1
    if empty == 0:
        return print(board)

    r,c = None,None
            
    for r_index, r_value in enumerate(board):
        if '' in r_value:
            r,c = r_index, r_value.index('.')
            break
            
    if r != None:
        for num in range(1,10):
                            
            pos = possible(board,str(num),r,c)

            if pos == True:
                board[r][c] = str(num)
                solveSudoku_allAns(board)
                board[r][c] = '.'

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def convert(arr): #convert array to Linked List 
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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def addTwoNumbers2(l1,l2):

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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(l1,l2):

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
        
        
    def divide(curr,leftbound,rightbound): #leftbound and rightbound is index range of curr relative to nums
        #1. break the array to left and right
        #2. check 

        left, right = curr[:len(curr)//2], curr[len(curr)//2:]
        left_compare, right_compare = left[-1], right[0]

        if target == left_compare: #target found!
            return leftbound + len(left) - 1

        elif target == right_compare: #target found!
            return leftbound + len(left)

        #target must be in left somewhere, in right somewhere, or doesnt exist
        elif target > right_compare:
            return divide(right,leftbound+len(left),rightbound)

        elif target < left_compare:
            return divide(left,leftbound,rightbound-len(right))

        else: #target doesnt exist
            return leftbound + len(left)

    return divide(nums,0,len(nums)-1)

#Date: June 19, 2021
#Given the head of a linked list, REMOVE the nth node from the end of the list and return its head.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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

#Date: June 22, 2021 
#Given the root of a binary tree, determine if it is a valid binary search tree (BST).
#A valid BST is defined as follows:
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

def isValidBST(root):
        
    #a preorder DFS method; if any node ever fails to meet definition of BST in its sub-tree, we return false
    #Note: float('inf') and float('-inf') are indefinely large and small float values
        
    if root == None: #reached bottom of a branch
        return True 
        
    if root.val <= largerThan or root.val >= lessThan:
        return False
        
    return isValidBST(root.left, root.val, largerThan) and \
           isValidBST(root.right, lessThan, root.val)
           #if we proceed left, all children nodes must <= current node from now and on
           #if we proceed right, all children nodes must >= current node from now and on

#Date: June 25, 2021 
#You are a professional robber planning to rob houses along a street.
#Each house has a certain amount of money stashed,
#the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected
#and it will automatically contact the police if two adjacent houses were broken into on the same night.
#Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums): #Brute force and bad time complexity
        
    #use recursion (starting from an initial house) and 
    #branch possibilities of next house by index order. We will then find the maximum sum stolen 
    #and return it as the answer.
        
        
    #special case (no input)
    if nums == []:
        return 0
        
    ans = []
        
    def next_house(start,house_index,total):                  
        ans.append(total)
        return
            
        for i,money in enumerate(nums[house_index + 2:]): #branching out to next possible houses
                
            next_house(start,house_index + 2 + i, total + money)
        
    for i,first in enumerate(nums[0:2]): #we start with first two houses because you cant go from house 0 --> 1 or 1 --> 2
                                         #but aside from that, you can jump to the same houses from these start points; starting at each house would be redundant
        next_house(i,i,first)
            
    return max(ans)

#alternative
def rob2(nums):

    #use dynamic programming to break the array into "sub-problems" O(n)
    #while traversing the array, we keep track of MAX AMOUNT THAT CAN BE ROBBED UP TO THE CURRENT HOUSE WE'RE ON (using 'total' array)
        
    #to do that, we consider 3 indices/houses of nums at a time to take into account
    #adjacent houses that cant be robbed, but might hold more money (total sum-wise up to that point) than the current total.
        
    #https://www.youtube.com/watch?v=73r3KWiEvyk

    #special conditions
    if len(nums)==0:
        return 0
    if len(nums) == 1 or len(nums) == 2:
        return max(nums)
			
    total = [max(nums[0:i]) for i in range(1,3)] #setting up first 2 indices of dp array

    for i in range(2, len(nums)):
        total.append(max(nums[i] + total[i-2], total[i-1])) #Should we skip the current house and stick with the maximum amount up to the last house,
                                                            #or add the money in the current house the maximum amount
                                                            #up to the second last house (to decide maximum up to the current house)??
        
    return total[-1]

#Date: June 29, 2021
#You are given an array prices where prices[i] is the price of a given stock on the ith day.
#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def maxProfit(prices):
        
    #O(n^2) time (pretty slow run time)
    #iterate through each day and check every day that follows to determine each possible "profit"; we keep track of max profit at all times
        
    max_profit = 0
    count = 0
        
    while count <= len(prices) - 2: #stop on second last day
            
        buy = prices[count]
            
        for sell in prices[count + 1:]:
            max_profit = max(max_profit, sell-buy)
            
        count += 1
        
    return max_profit

#alternative
def maxProfit2(prices):
    #O(n) traversal solution
    #we keep track of minimum price (transient) as we iterate through the array, and find possible profits given that minimum price
    #this also insures that buying date < selling date chronologically
        
    minimum_buy = float('inf')
    max_profit = 0
        
    for price in prices:
        minimum_buy = min(minimum_buy,price)
        max_profit = max(max_profit, price - minimum_buy)
        
    return max_profit

#Date: July 2, 2021
#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

def climbStairs(n):
        
    #an O(n) approach using dynamic programming
    #we base the code mainly on the fact that climbStairs(n) = climbStairs(n-1) + climbStairs(n-2);
    #the only ways to get directly onto the nth step is from the n-1th or n-2th.
        
    #special case
    if n <= 2:
        return n
        
    dp = [1,2]
    for step in range(2,n):
        dp[0], dp[1] = dp[1], dp[0] + dp[1] #we replace the values instead of appending to end of array to avoid O(n) worst scenario
        
    return dp[-1]

#Date: July 3, 2021 
#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Your goal is to reach the last index in the minimum number of jumps.
#You can assume that you can always reach the last index.

def jump(nums):
        
    #an intuitive O(n^2) brute force/dynamic programming solution
    #in essence we want to find the smallest # of jumps to each index and eventually make our way to the end.
    #to accomplish this, we will loop through each index in 'nums' while checking all
    #possible positions that we can jump to from that particular index; we keep track of the least amount of jumps that
    #we need to reach each visited index in a hash table.
        
    ans = {n: float('inf') for n in range(0,len(nums))} 
    ans[0] = 0
        
    if len(nums) == 1:
        return 0
        
    for start,max_jump in enumerate(nums):
        for end in range(start+1, start+max_jump+1): #visiting each possible index we can jump to 
                
            ans[end] = min(ans[end], ans[start] + 1) #we use min() incase the index we jumped to has already been visited with a smaller # of jumps.
                
            if end == len(nums) - 1: #our return condition; if we reach the end
                return ans[end]
            
#alternative with better time complexity
def jump2(nums):
    #The idea is to maintain a transient frame between two pointers: left and right,
    #which represent a range of indexes that can be reached with a minimum of 'x' jumps.
    #Left initialy set to be 0 and right set to be nums[0]. Hence, points between 0 and nums[0]
    #can be reached using just 1 jump. Next, we want to find points I can reach using 2 jumps... and so on;
    #our new left will be set equal to right, and our new right will be set equal to the farest point we
    #can reach by two jumps. which is:

    #right = max(i + nums[i] for i in range(left, right + 1)

    if len(nums) == 1: 
        return 0
        
    left, right = 0, nums[0]
    jumps = 1
        
    while right < len(nums) - 1:
        jumps += 1
        nxt_right = max([i + nums[i] for i in range(left, right + 1)]) #furtherst of all possible next positions 
        left, right = right, nxt_right
            
    return jumps

#Date: July 6, 2021
#Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permute(nums):
        
    #recursive DFS approach; approximately O(2^n) time due to recursive call stack
    #base case: when permutation length = nums = length
    #arguments: current permutation, whats left in nums for us to use
        
    ans = []
        
    def helper(curr, remaining):
        
        if len(remaining) == 0: #base case; theres nothing left to add to the permutation
            ans.append(curr)
            return
          
        for i, next_elem in enumerate(remaining): #add each possible "next value" to the current permutation and recurse
            helper(curr + [next_elem], remaining[:i] + remaining[i+1:])
          
        
    helper([],nums)
        
    return ans

#Date: July 7, 2021
#Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

def permuteUnique(nums):
    
    #dfs + dynamic programming solution
    #similar solution to previous question. However, each time we add the next layer to
    #each individual permutation we check if a particular number has already been used (avoids duplicates and unecessary run time) through a hash table.
        
    res = []
                
    def dfs(nums, path, res):
        
        used = {}

        if not nums: #base case to stop the dfs recursion
            res.append(path)
            return

        for i in range(len(nums)):

            if used.get(nums[i]):
                continue #returns to begenning of loop while ignoring rest of the code
                    
            used[nums[i]] = True
            dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
                
    dfs(nums, [], res)
    return res

#Date: July 9, 2021
#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

def groupAnagrams(strs):
        
    #to approach this we must note that all anagrams will produce the same string if sorted
    #with that in noted, we can group anagrams together with a hash table when traversing 'strs'; the key will be the sorted anagram and the value will the anagrams
        
    res = {}
        
    for word in strs:
            
        if not res.get(temp := tuple(sorted(word))): #we use a tuple over an array because its hashable
            res[temp] = [word]
            continue
            
        res[temp].append(word)
        
    return res.values()

#Date: July 10, 2021
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

def maxSubArray(nums):
    #an iterative dynamic programming approach O(n)
        
    #we initialize a current subarray to start at nums[0], for every next index we may either choose to keep its value in our current subarray,
    #or choose to start a new subarray at that value.
    #if we choose to keep the value (if value + current sum of subarray > value), we add the value to the sum of our current subarray
    #otherwise, we will start a new subarray at nums[i]
        
    #to actually solve the question however, it is important to note,that we will keep track of our desired answer (contiguous subarray with largest sum)
    #by comparing the current sum of each subarray at every index and keeping track of the max value. 
        
    sub_array_sum = nums[0] #sum of current subarray, from a particular start index to another index (both currently 0)
    res = nums[0]
        
    for i in range(1,len(nums)):
        sub_array_sum = max(sub_array_sum + nums[i], nums[i]) #in this context, nums[i] marks a potential start to a new subarray
        res = max(res, sub_array_sum)
        
    return res

#Date: July 11, 2021
#Given an m x n matrix, return all elements of the matrix in spiral order.

def spiralOrder(matrix):
        
    #an O(n) solution where n is number of total elements
    #while the matrix still holds element, we peel layers in this sequence:
    #1.top row (rightwards), 2.right (downwards), 3.bottom (leftwards), 4.left (upwards)
        
    ans = []
        
    def done(matrix):
            
        if len(matrix) == 0: #either whole matrix is empty
            return True
            
        count = 0 #or every array in the matrix is empty
        for arr in matrix:
            if len(arr) != 0:
                count += 1
        if count == 0:
            return True
            
        return False
        
    while True:
            
        #1.
        ans += [j for j in matrix[0]]
        matrix.pop(0)
            
        if done(matrix):
            return ans
            
        #2.
        ans += [j[-1] for j in matrix]
        for row in matrix:
            row.pop()
                
            if done(matrix):
                return ans
            
        #3.
        ans += [matrix[-1][i*-1] for i in range(1,len(matrix[-1])+1)]
        matrix.pop()

        if done(matrix):
            return ans
                     
        #4.
        ans += [matrix[i*-1][0] for i in range(1,len(matrix)+1)]
        for row in matrix:
            row.pop(0)
                
        if done(matrix):
            return ans
            
    return ans

#Date: July 13, 2021
#Given a linked list, swap every two adjacent nodes and return its head.
#You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def swapPairs(self):

    #5 step solution: iterate through 2 nodes at a time always have shallow copies of: the first node, the second node, and the node previous to the first node
        
    prev = dummy = ListNode()
    curr = dummy.next = head
        
    while curr and curr.next:
            
        first = curr
        second = curr.next
            
        #1.
        first.next = second.next
            
        #2.
        prev.next = second
            
        #3.
        second.next = first
            
            
        #4/5.
        prev = second.next
        curr = prev.next
            
        
    return dummy.next

#Date: July 17, 2021
#Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
#Each element in the array represents your maximum jump length at that position.
#Determine if you are able to reach the last index.

def canJump(nums):
        
    #An O(n) traversal solution; we continuously update the maximum index we can potentially reach, up to and including a particular index.
    #if an index within the nums is ever beyond our max reach --> its impossible to reach the end. 
        
    max_reach = 0
        
    for i, j in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i+j)
            
    return True

#Date: July 18, 2021
#Given an array of intervals where intervals[i] = [starti, endi],
#merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
        
    #an O(n^2*log n) solution
    #Assuming starting point of intervals are increasing... we will start with one initial (current) interval to focus on,
    #and traverse the remaining intervals while checking the following:
        
    #1. if start > current end --> add new interval
    #2. if start <= current end and end > current end --> current end = end
        
    intervals = sorted(intervals, key=lambda x: x[0])
    ans = [intervals[0]]
        
    for i in range(1, len(intervals)):
            
        if intervals[i][0] > ans[-1][1]:
            ans.append(intervals[i])
            
        elif intervals[i][1] > ans[-1][1]:
            ans[-1][1] = intervals[i][1]
        
    return ans

#Date: July 19, 2021
#Given a string s consists of some words separated by spaces,
#return the length of the last word in the string. If the last word does not exist, return 0.
#A word is a maximal substring consisting of non-space characters only.

def lengthOfLastWord(self, s: str) -> int:
        
    #An O(n) solution; traverse the string backwards and stop when we see a space and + have already seen a non-space character in the past 
        
    seen_char = False
    count = 0
        
    for i in range(1,len(s)+1):
            
        if seen_char and s[i*-1] == ' ':
            return count
            
        if s[i*-1] != ' ':
            seen_char = True
            count += 1
        
    return count

#Date: July 20, 2021
#You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
#Merge all the linked-lists into one sorted linked-list and return it.

def mergeKLists(lists):
        
    #A O(2n+nlog n) --> O(n+nlog n) solution
    #Change into array data structure, sort, then convert back
        
    temp = []
        
    def ll_to_arr(head):
        curr = head
        while curr:
            temp.append(curr.val)
            curr = curr.next
        
    def arr_to_ll(arr):
        curr = dummy = ListNode()
        for x in arr:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next
                
    for head in lists:
        ll_to_arr(head)
    temp.sort()
        
    return arr_to_ll(temp)

#Date: July 20, 2021
#Given a positive integer n, generate an n x n matrix filled with elements from 1 to n^2 in spiral order.

def generateMatrix(n):
        
    #keep track of our position (i.e row, column) in the matrix and traverse in the following order: right, down, left, up
        
    #we change directions given two cases:
    #1. we receive an index error (we went outside of the given dimensions)
    #2. we have reached a spot that has already been filled
              
    matrix = [[None for x in range(0,n)] for y in range(0,n)]
        
    curr, filled = [0,-1], 0 
    #[row, column]

       
    while filled < n*n:
            
        #right
        curr[1] += 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[1] += 1
                    
                else:
                    curr[1] -= 1
                    break
                
            except IndexError:
                curr[1] -= 1
                break
            
            
        #down
        curr[0] += 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[0] += 1
                    
                else:
                    curr[0] -= 1
                    break
                
            except IndexError:
                curr[0] -= 1
                break
            
            
        #left
        curr[1] -= 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[1] -= 1
                    
                else:
                    curr[1] += 1
                    break
                
            except IndexError:
                curr[1] += 1
                break
            
        #up
        curr[0] -= 1
        while True:
            try:
                if not matrix[curr[0]][curr[1]]:
                    matrix[curr[0]][curr[1]] = filled + 1
                    filled += 1
                    curr[0] -= 1
                    
                else:
                    curr[0] += 1
                    break
                
            except IndexError:
                curr[0] += 1
                break
                        
    return matrix

#Date: July 23, 2021 
#Given the head of a linked list, rotate the list to the right by k places.

def rotateRight(head,k):
        
    #O(kn) time; worst case of O(n^2) time.
    #for each rotation we traverse to the end of the linked list and bring the last node to the head
    #the minimum number of iterations/rotations needed is calculated by:

    #round(((k / length) - (k // length)) * length), where length is the length of the linked list
      
        
    if (not head) or (not head.next):
        return head
        
    def len_ll(head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next      
        return count
        
    length = len_ll(head)
    iterations = round(((k / length) - (k // length)) * length)
            
    for x in range(0,iterations):
            
        curr = head
        while curr.next.next:
            curr = curr.next
            
        hold = curr.next
        curr.next = None
        hold.next = head
        head = hold
            
    return head

#Date: July 24, 2021
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#How many possible unique paths are there?

def uniquePaths(m,n):

    #an O(mn) time dynammic programming approach
    #possbilities of getting to matrix[row][column] = matrix[row-1][column] + matrix[row][column-1]
        
    matrix = [[1] + [None for i in range(0,n-1)] for j in range(0,m)]
    matrix[0] = [1 for i in range(0,n)]
        
    for r in range(1,m):
        for c in range(1,n):
            matrix[r][c] = matrix[r][c-1] + matrix[r-1][c]
        
    return matrix[m-1][n-1]

#Date: July 25, 2021
#A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#The robot can only move either down or right at any point in time.
#The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#Now consider if some obstacles are added to the grids. How many unique paths would there be?
#An obstacle and space is marked as 1 and 0 respectively in the grid.

def uniquePathsWithObstacles(obstacleGrid):
        
    #O(3mn + m) time
    #1. we first traverse the matrix to convert all the 0s to 1s and vice versa
    #2. from there, we need to add an additional layer of of 0s to wrap the top and left of the matrix to overcome situations where there obstacles blockade an entire row
    #3. ultimately we will traverse the matrix and take the same approach as the previous question

    #3.
    def helper(matrix,m,n):
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][c] != 0 and (r!=1 or c!=1):
                    matrix[r][c] = matrix[r][c-1] + matrix[r-1][c]

        return matrix[-1][-1]

    #1. 
    for r in range(0,rows:=len(obstacleGrid)):
        for c in range(0,cols:=len(obstacleGrid[0])):     
            if obstacleGrid[r][c] == 1: obstacleGrid[r][c] = 0
            else: obstacleGrid[r][c] = 1

    #2.
    for r in range(0,rows):
        obstacleGrid[r].insert(0,0)
    obstacleGrid.insert(0,[0 for i in range(0,cols+1)])
        

    return helper(obstacleGrid, rows+1, cols+1)

#Date: July 26, 2021
#Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
#Note: You can only move either down or right at any point in time.

def minPathSum(grid):
        
    #dynamic programming O(mn + m + n) time solution
    #minPathSum(grid[r][c]) = minimum of current box + top box and current box + left box
        
    #initialize the first row to be all 1s
    for r in range(1,rows:=len(grid)):
        grid[r][0] = grid[r][0] + grid[r-1][0]
        
    #initialize the first column to be all 1s
    for c in range(1,cols:=len(grid[0])):
        grid[0][c] = grid[0][c] + grid[0][c-1]
        
    for r in range(1,rows):
        for c in range(1,cols):
            grid[r][c] = min(grid[r][c]+grid[r-1][c], grid[r][c]+grid[r][c-1])
        
    return grid[-1][-1]

#Date: July 27, 2021
#Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
#The digits are stored such that the most significant digit is at the head of the list, and each element in the array contains a single digit.
#You may assume the integer does not contain any leading zero, except the number 0 itself.

def plusOne(digits):
        
    #Best time: O(1), average time: O(n), worst case: O(2n)
        
    for i in range(1,len(digits)+1):
            
        digits[i*-1] = digits[i*-1] + 1
            
        #if there isnt any digit to carry over, we are finished
        if len(str(digits[i*-1])) == 1:
            return digits
            
        #if there is a digit to carry over but we are already on the 0th index, we insert and extra 1 in the front of the array
        elif i == len(digits):
            digits[0] = 0
            digits.insert(0,1)
            return digits
            
        #if there is a digit to carry over, we add it to the previous index
        else:
            digits[i*-1] = digits[i*-1] - 10
    return

#Date: July 28, 2021
#Given two binary strings a and b, return their sum as a binary string.

def addBinary(a,b):
        
    #1. make sure the two binary strings are of equal length
    if (l_a := len(a)) > (l_b := len(b)): 
        b = ''.join(['0' for i in range(0,l_a-l_b)]) + b
            
    if l_b > l_a: 
        a = ''.join(['0' for i in range(0,l_b-l_a)]) + a
        
    #2. do the addition digit-by-digit by traversing backwards
    #ans has length of len(a) + 1 in case the last digit has a carry-over
    ans = ['0' for i in range(0,len(a)+1)]
    for i in range(-1,-1*(1+len(ans)),-1):
            
        if i > -1*len(ans):
            ans[i] = str(int(ans[i]) + int(a[i]) + int(b[i]))
            
        #situation adressing a possible carry-over to the next digit
        if int(ans[i]) > 1:
            ans[i-1],ans[i] = str(divmod(int(ans[i]),2)[0]), str(divmod(int(ans[i]),2)[1])
        
    if ans[0] == '0': return ''.join(ans[1:])
    return ''.join(ans)

#Date: July 29, 2021
#Given a non-negative integer x, compute and return the square root of x.
#Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

#Note: You are not allowed to use any built-in exponent function or operator,

def mySqrt(x):
        
    #An O(log n) time divide and conquer solution
    #we have a transient range of numbers for which the answer could be in, and continuously evaluate the average of the range (num) to be the potential solution
    #if it occurs that num is too large, we cut the range down to the smaller half; and vice versa if num is too small
        
    frame = [0,(x//2)+2]
    num = (frame[0] + frame[1]) // 2
        
    while True:
        
        if num * num <= x and (num+1) * (num+1) > x:
            return num
            
        elif num * num < x:
            frame = [num, frame[1]]
            num = (frame[0] + frame[1]) // 2
            
        else:
            frame = [0,num]
            num = (frame[0] + frame[1]) // 2

#Date: July 29, 2021:
#Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

def myPow(x,n):
        
    #An optimized recursive solution
        
    if not n:
        return 1
        
    if n < 0: #a^-b = 1/a^b
        return 1 / myPow(x, -n)
        
    if n % 2 == 1: 
        return x * myPow(x, n-1)
        
    return myPow(x*x, n/2) #since a^b = (a^2)^b/2; this is done for the sake of optimization

#Date: July 29, 2021
#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
        
    #An average O(n^2) time traversal solution with memoization
    #for each 0 we encounter, we update the entire row and column to 0s, but on the condition that the row/column has not been updated yet
        
    row_cache = {}
    column_cache = {}
        
    for r in range(0,rows := len(matrix)):
        for c in range(0,cols := len(matrix[0])):
    
            if matrix[r][c] == 0:
                    
                if not row_cache.get(r):
                    for i in range(0,cols):
                        if matrix[r][i] != 0:
                            matrix[r][i] = '0' #we use strings so we only consider the initial 0s
                    row_cache[r] = True
                    
                if not column_cache.get(c):
                    for i in range(0,rows):
                        if matrix[i][c] != 0:
                            matrix[i][c] = '0'
                    column_cache[c] = True
    return

#Date: July 29, 2021
#Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

#1. Integers in each row are sorted from left to right.
#2. The first integer of each row is greater than the last integer of the previous row.

def searchMatrix(matrix):
        
    #An O(log n) divide and conquer solution
    #by using an upper/lower range and assuming that target exists, divide and conquer on a 2D scale, then on a 1D scale once you've narrowed down one row the target is located in
    #if at any point target gets caught right between the upper/lower range, return False
        
    while len(matrix) > 1:
            
        div = len(matrix) // 2 #divides the upper/lower range
            
        if target == matrix[div-1][-1] or target == matrix[div][0]:
            return True
              
        elif target < matrix[div-1][-1]:
            matrix = matrix[:div]
            
        elif target > matrix[div][0]:
            matrix = matrix[div:]
            
        else:
            return False
        
    matrix = matrix[0]
    while len(matrix) > 1:
            
        div = len(matrix) // 2
            
        if target == matrix[div-1] or target == matrix[div]:
            return True
            
        elif target < matrix[div-1]:
            matrix = matrix[:div]
            
        elif target > matrix[div]:
            matrix = matrix[div:]
            
        else:
            return False
        
    if matrix[0] == target:
        return True
    return False

#Date: July 31, 2021
#Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#You must solve this problem without using the library's sort function.

def sortColors(nums):
        
    """
    Do not return anything, modify nums in-place instead.
    """
    #Dutch flag algorithm; one-pass and O(n) time
    #other feasible solutions: bubble sort O(n^2), insertion/selection sort O(2n)
        
    low,mid,high = 0,0,len(nums)-1
        
    while mid <= high:
            
        if nums[mid] == 0:
            nums[mid],nums[low] = nums[low],nums[mid]
            low += 1
            mid += 1
         
        elif nums[mid] == 1:
            mid += 1
            
        else:
            nums[mid],nums[high] = nums[high],nums[mid]
            high -= 1

#August 1, 2021:
#Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].
#You may return the answer in any order.

def combine(n,k):
        
    #A dfs recursive approach
    #we build each combination (curr) individually - one number per call
    #a new recursive call must add on a number greater than the previous to the current combination (this is to avoid creating overlaps/permutations instead of combinations)
        
        
    res = []
        
    def dfs(rem, curr):
            
        if len(curr) == k:
            res.append(curr)
            return 
            
        for i in range(len(rem)):
            dfs(rem[i+1:], curr+[rem[i]])
        
    dfs([x for x in range(1,n+1)], [])
    return res

#August 2, 2021:
#Given an integer array nums of unique elements, return all possible subsets (the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.

def subsets(nums):
        
    #a dfs recursive solution
    #the same approach as the previous question besides the prodcedure of appending our current combination to the global answer on every recursive call
        
    ans = []
        
    def dfs(curr,rem):
            
        ans.append(curr)
        if rem == 0:
            return
            
        for i in range(0,len(rem)):
            dfs(curr+[rem[i]], rem[i+1:])
    
    dfs([],nums)
    return ans

#August 3, 2021
#Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(head):
        
    #An O(n) traversal solution
    #We keep track of all seen values in a hash table 
    #if we come across a value that has already be seen, we remove it
        
    seen = {}
    prev = None
    curr = head
        
    while curr:
            
        if not seen.get(curr.val):
            seen[curr.val] = True
            prev = curr
            curr = curr.next
            
        else:
            curr = curr.next
            prev.next = curr
        
    return head

#Date: August 4, 2021
#Given an m x n grid of characters board and a string word, return true if word exists in the grid.
#The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
#The same letter cell may not be used more than once.

def exist(board,word):
        
    #A recursive dfs solution
    #From each position on the board, we branch out possible paths to neighboring cells that might contain the word;
    #for each recursive branch, we keep track of the matched characters (of the word), and the traversed positions (so we dont traverse the same cell twice).
        
    #1. if at any point the current position on the board mismatches the word, we halt the current recursive branch 
        
    #2. if all characters of the word are matched, we update the global answer (to be returned) to true
          
    ans = False
        
    def dfs(r,c,pointer,traversed):
            
        nonlocal ans
                
        if board[r][c] == word[pointer]:
                
            if pointer == len(word)-1:
                ans = True
                return
                
            #right
            if c < len(board[0])-1 and not traversed.get((r,c+1)):
                traversed[(r,c+1)] = True
                dfs(r,c+1,pointer+1,traversed)
                traversed.pop((r,c+1))
                    
            #left
            if c > 0 and not traversed.get((r,c-1)):
                traversed[(r,c-1)] = True
                dfs(r,c-1,pointer+1,traversed)
                traversed.pop((r,c-1))
                    
            #up
            if r > 0 and not traversed.get((r-1,c)):
                traversed[(r-1,c)] = True
                dfs(r-1,c,pointer+1,traversed)
                traversed.pop((r-1,c))
                
            #down
            if r < len(board)-1 and not traversed.get((r+1,c)):
                traversed[(r+1,c)] = True
                dfs(r+1,c,pointer+1,traversed)
                traversed.pop((r+1,c))
        return
        
    for i in range(0,len(board)):
        for j in range(0,len(board[0])):
            dfs(i,j,0,{(i,j):True})
    return ans

#August 5, 2021
#Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

def maximalRectangle(matrix):
        
    #we will traverse the matrix; for each '1' we encounter, we will initialize a rectangle with dimensions of 1x1 initially
    #sequentially, we will push the width and height of the rectangle as far right/down as possible while possible. 
    #this allows us to find the area of all rectangles in the matrix - from which we can then deduce the maximum area
        
    areas = [0]
        
    #push down
    def push_down(start,end,curr_row,row,cols):
        areas.append(cols*row)
        if curr_row < len(matrix)-1 and all(n == '1' for n in matrix[curr_row+1][start:end+1]):
            push_down(start,end,curr_row+1,row+1,cols)
        
    #push right
    def push_right(i,j):
        temp_j = j
        cols = 1
        while temp_j < len(matrix[0]) and matrix[i][temp_j] == '1':
            push_down(j,temp_j,i,1,cols)
            temp_j += 1
            cols += 1
        
    for i in range(0,len(matrix)):
        for j in range(0,len(matrix[0])):
            if matrix[i][j] == '1':
                push_right(i,j)
        
    return max(areas)

#August 5, 2021
#Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#You should preserve the original relative order of the nodes in each of the two partitions.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def partition(head,x):
        
    #An O(n) traversal solution using dummy nodes and external memory
    #we group together all node values < x in one linked list, and all other nodes in another linked list while preserving their "relative positions"
    #ultimately, we will join together the two lists in their respective order (smaller nodes --> other nodes)
        
    curr_o = others = ListNode()
    curr_s = smaller = ListNode()
    curr = head
        
    while curr:
            
        if curr.val < x:
            curr_s.next = ListNode(curr.val)
            curr_s = curr_s.next
            
        else:
            curr_o.next = ListNode(curr.val)
            curr_o = curr_o.next
                
        curr = curr.next
                
    curr_s.next = others.next
    return smaller.next

#August 5, 2021
#You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
#representing the number of elements in nums1 and nums2 respectively.

#Merge nums1 and nums2 into a single array sorted in non-decreasing order.

#The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

def merge(nums1,n,nums2,m):
    """
    Do not return anything, modify nums1 in-place instead.
    """
        
    #intuitive O('n' + nlogn) time solution
        
    nums1[m:] = nums2[:n]
    nums1.sort()

#August 7, 2021:
#Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseBetween(head):
        
    #an O(n) traversal solution
    #we divide the linked list into 3 sections using dummy nodes: left/right of the section (left-right) of interest, and the section of interest itself
    #regarding the section of interest in particular, we will reverse the desired portion of the linked list as we traverse it
    #finally, we'll concatenate the 3 sections together and return the result
        
    l_trav = l = ListNode(0)
    sec = None
    r_trav = r = ListNode(0)
    hold = None
        
    curr,node = head,1
    while curr:
            
        if node < left:
            l_trav.next = ListNode(curr.val)
            l_trav = l_trav.next
                
        elif node > right:
            r_trav.next = ListNode(curr.val)
            r_trav = r_trav.next
            
        else:
            sec, sec.next= ListNode(curr.val), sec

            if node == left:
                hold = sec
                
        curr = curr.next
        node += 1
        
    l_trav.next = sec
    hold.next = r.next
       
    return l.next

#Date: August 8, 2021
#Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s. You can return them in any order.
#A valid IP address consists of exactly four integers, each integer is between 0 and 255, separated by single dots and cannot have leading zeros.
#For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 

def restoreIpAddresses(s):
        
    #a dfs solution
    #we seek to insert the dots in the given string one at a time to form a potentially valid adress
    #we able to insert a dot at a given index under the following coditions:
        #1. there will be enough characters remaining to insert the remaining dots (e.g we can only insert the first dot if there at a minimum of 3 characters that will follow the dot)
        #2. the integer that comes before the dot must have a maximum of 3 characters between 0 and 255
        #3. the integer in question must to start with a 0
    #Once, we've inserted 3 valid dots, we append our current possibility to an array of solutions
                
    ans = []
        
    def dfs(curr,dot,depth):
            
        if depth == 3:
            if curr[dot:] != '' and int(curr[dot:]) >= 0 and int(curr[dot:]) <= 255:
                if not (len(curr[dot:]) >= 2 and curr[dot] == '0'):
                    ans.append(curr)
                    return
            return
            
        for i in range(dot+1,dot+4):
            if len(curr[i:]) >= 3-depth:
                if int(curr[dot:i]) >= 0 and int(curr[dot:i]) <= 255:
                    if not (len(curr[dot:i]) >= 2 and curr[dot] == '0'): 
                        dfs(curr[:i] + '.' + curr[i:],i+1,depth+1)
                     
    dfs(s,0,0)
    return ans

#Date: August 9, 2021
#Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def postorderTraversal(root):
        
    ans = []
        
    def dfs(node):
            
        nonlocal ans
            
        if node:
            dfs(node.left)
            dfs(node.right)
            ans += [node.val]
                
    dfs(root)
    return ans

#Date: August 9, 2021
#Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def inorderTraversal(root):
        
    ans = []
        
    def dfs(node):
            
        nonlocal ans
            
        if node:
            dfs(node.left)
            ans += [node.val]
            dfs(node.right)
                  
    dfs(root)
    return ans

#Date: August 9, 2021
#Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def preorderTraversal(root):
        
    ans = []
        
    def dfs(node):
            
        nonlocal ans
            
        if node:
            ans += [node.val]
            dfs(node.left)
            dfs(node.right)
                  
    dfs(root)
    return ans

#August 10, 2021
#Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSameTree(p,q):
        
    #a bfs solution
    #we check both trees simultaneously - one layer at a time
    #if at any point, the layers do not match up, the answer is falsified
    #if both layers comprise only of None valued nodes (meaning we cleared the whole tree), we return true
        
    if p == None:
        p = TreeNode(None)
    if q == None:
        q = TreeNode(None)
            
    def next_layer(layer):
            
        for i in range(0,len(layer)):
                
            if type(layer[i].val) == int:
                if layer[i].left:
                    layer += [layer[i].left]
                else:
                    layer += [TreeNode(None)]
                if layer[i].right:
                    layer += [layer[i].right]
                else:
                    layer += [TreeNode(None)]
            else:
                layer += [TreeNode(None), TreeNode(None)]
            
        return layer
            

    def bfs(p_layer, q_layer):
            
        if any(p_layer[i].val != q_layer[i].val for i in range(0,len(p_layer))):
            return False
        elif all(node.val == None for node in p_layer + q_layer):
            return True
            
        prev = len(p_layer)
        p_layer, q_layer = next_layer(p_layer), next_layer(q_layer)
                    
        return bfs(p_layer[prev:],q_layer[prev:])
                
    return bfs([p],[q])

#August 12, 2021
#You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake.
#Recover the tree without changing its structure.
#Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def recoverTree(root):
        
    """
    Do not return anything, modify root in-place instead.
    """
        
    #inorder dfs solution; we will exploit the fact that the an INORDER dfs traversal for a binary tree will always return
    #the node values in increasing order due to its nature
    #thus, given the two nodes we will need to swap, 
    #[1] the first node will always be greater then its next node, 
    #and [2] the second node will always be smaller than its previous node. 
    #Otherwise, there will be more than one swap required - which is impossible.
        
    node1 = None
    node2 = None
    prev = TreeNode(float(-inf))
        
    def dfs(node):
            
        nonlocal node1, node2, prev
            
        if node:
            dfs(node.left)
                
            if not node1 and prev.val >= node.val: #[1]
                node1 = prev
                
            if prev.val >= node.val: #[2]
                node2 = node
                
            prev = node
                
            dfs(node.right)
        return
        
    dfs(root)
    node1.val,node2.val = node2.val,node1.val
    return

#Date August 13, 2021
#Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSymmetric(root):
    
    #a dfs traversal solution, starting from the children of the root node, we compare each set of symmetrical nodes by recursing with the outer pair and inner pair of the current node 
    #if all pairs have cleared the tree without having been falsified, we return True
    
    if root == None:
        return True
    return Mirror(root.left, root.right)

def Mirror(left, right):
        
    if left == None and right == None:
        return True
    if left == None or right == None:
        return False

    if left.val == right.val:
        outPair = Mirror(left.left, right.right)
        inPiar = Mirror(left.right, right.left)
        return outPair and inPiar
    return False

#Date: August 16, 2021
#Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def levelOrder(root):
        
    #a layer-by-layer bfs traversal. 
        
    res = []
        
    if root == None:
        return []
        
    def bfs(layer):
            
        nonlocal res
        if layer == []:
            return
            
        res.append([n.val for n in layer])
            
        for i in range(0,prev := len(layer)):
                
            if layer[i].left:
                layer += [layer[i].left]
                
            if layer[i].right:
                layer += [layer[i].right]
        bfs(layer[prev:])
            
    bfs([root])
    return res

#Date: August 17, 2021
#Given the root of a binary tree, return the zigzag level order traversal of its nodes' values.
#(i.e., from left to right, then right to left for the next level and alternate between).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def zigzagLevelOrder(root):
        
    #a bfs solution; however, we iterate through the nodes from each layer in reverse order to how they were appended and create the next layer, through either a node.left -> node.right -> next node or a node.right -> node.left -> next node parrtern, while iterating through the current layer#
        
    #take the binary tree [3,9,20,null,null,15,7] for instance
        
    #layer 0: root
    #layer 1: iterating in reverse [3] => [20,9]
    #layer 2: iterating in reverse [20,9] => [15,7]
        
    def check_left(node):
        if node.left:
            return node.left
        return None
        
    def check_right(node):
        if node.right:
            return node.right
        return None
            
    def helper(layer, count):
        
        nonlocal res
            
        if len(layer) == 0:
            return
            
        res.append([node.val for node in layer])
            
        temp = []
        for i in range(-1,-((len(layer))+1),-1):
   
            if count % 2 == 1:
                if check_right(layer[i]):
                    temp += [layer[i].right]
                if check_left(layer[i]):
                    temp += [layer[i].left]
                
            else:
                if check_left(layer[i]):
                    temp += [layer[i].left]
                if check_right(layer[i]):
                    temp += [layer[i].right]
                        
        helper(temp,count+1 )
        
    if root == None:
        return []
        
    res = []
        
    helper([root], 1)
    return res

#Date: August 18, 2021
#Given an integer n, return true if n has exactly three positive divisors. Otherwise, return false.
#An integer m is a divisor of n if there exists an integer k such that n = k * m.

import math
def isThree(n):
        
    #an O(n) solution; given that 1 and n must be factors of n, check for other possible factors from n till square root of n (to avoid overlap)
        
    divs = 2
        
    for i in range(2,int(math.sqrt(n))+1):
            
        if n/i == n//i:
            if i == math.sqrt(n):
                divs += 1
            else:
                divs += 2
        
    if divs == 3:
        return True
    return False

#Date: August 19, 2021
#Given the root of a binary tree, return its maximum depth.
#A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxDepth(root):
        
    #a pre-order traversal while keeping track of the current depth (which will allow the global answer to constantly be updated)
    
    ans = 0
        
    def dfs(node, depth):
        
        nonlocal ans
        
        ans = max(ans,depth)
        
        if node.left != None:
            dfs(node.left, depth+1)
        
        if node.right != None:
            dfs(node.right, depth+1)
        
        return
    
    if root != None:
        dfs(root,1)
        return ans
    return 0

#Date: August 22, 2021
#Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
#A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node NEVER DIFFERS BY MORE THAN ONE.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sortedArrayToBST(nums):
        
    #divide and conquer + recursion; for each recursive call, we assign the lower half of values to the left sub-tree and the other half to the right
        
    if not nums:
        return 
    
    mid = len(nums) // 2
    root = TreeNode(nums[mid])
    root.left = self.sortedArrayToBST(nums[:mid])
    root.right = self.sortedArrayToBST(nums[mid+1:])

    return root

#Date August 22, 2021
#Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
#Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def goodNodes(root):
        
    #preorder dfs + keeping track of max_value on each path 
    
    def helper(node,max_val):
        
        nonlocal good
        
        if node:
            if node.val >= max_val:
                good += 1

            helper(node.left,max(node.val,max_val))
            helper(node.right,max(node.val,max_val))        
        return 
    
    good = 0
    helper(root,float('-inf'))
    return good

#Date: August 22, 2021
#Given the root of a binary tree, invert the tree, and return its root.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    
    #preorder traversal: swap every pair of branches
    
    def dfs(node):
        
        if node:
            node.left,node.right = node.right,node.left
            dfs(node.left)
            dfs(node.right)
    
    dfs(root)
    return root

#Date: August 22, 2021
#Given a binary tree, find its minimum depth.
#The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def minDepth(root):
        
    def dfs(node,depth):
        nonlocal ans
        
        if node:
            if not (node.left or node.right):
                ans = min(ans,depth)
            
            dfs(node.left,depth + 1)
            dfs(node.right,depth + 1)
        return
    
    ans = float('inf')
    dfs(root,1)
    if not root: return 0
    return ans

#Date: August 22, 2021
#Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that
#adding up all the values along the path equals targetSum.
#A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def hasPathSum(root,targetSum):
        
    #preorder dfs; go down every possible path and check the sums

    def dfs(node,curr):
        nonlocal ans
        
        if node:
            
            if not (node.left or node.right) and curr == targetSum:
                ans = True
                return
            
            if node.left:
                dfs(node.left,curr+node.left.val)
            
            if node.right:
                dfs(node.right,curr+node.right.val)
    
    ans = False
    if not root: return False
    dfs(root,root.val)
    return ans
                    
    
