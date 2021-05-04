#Date: March 14, 2021
#Purpose: quick question I heard about

#Given a single array, determine the distance (in indices)
#between the value at each index and the closest greater value AHEAD.

#Note: return output for each index of the input array in the format of another array
#Note: if there is greater no value ahead of the current, then the output for that index is 'impossible'.

def GreaterValues(arr):
    #use stack, always keep smallest value in front (will be automatically done)
    #if a value is larger than smallest value, compare then repeat if necesarry

    ans = arr
    stack = []
    
    for index, value in enumerate(arr):

        #initialize the stack when its first index
        if index == 0:
            stack.append((value,index))

        #if less or equal to most recent
        if value <= stack[-1][0] and index != 0 :
            stack.append((value,index))
        

        #if bigger than most recent/smallest
        elif value > stack[-1][0]:

            while value > stack[-1][0] and len(stack) > 0:
                ans[stack[-1][1]] = (index - stack[-1][1], 'possible')
                stack.pop()

                try: #if it is bigger than every value in the stack, then go onto next round
                    stack[-1][0]
                
                except IndexError:
                    break

            stack.append((value,index))

    for index, element in enumerate(ans):
        if type(element) != tuple:
            ans[index] = 'impossible'

    return ans
