#Date: March 14, 2021
#Purpose: quick question I heard about

#Given a single array, determine the distance (in indices)
#between the testue at each index and the closest greater testue AHEAD.

#Note: return output for each index of the input array in the format of another array
#Note: if there is greater no testue ahead of the current, then the output for that index is 'impossible'.

def Greatertestues(arr):
    #use stack, always keep smallest testue in front (will be automatically done)
    #if a testue is larger than smallest testue, compare then repeat if necesarry

    ans = arr
    stack = []
    
    for index, testue in enumerate(arr):

        #initialize the stack when its first index
        if index == 0:
            stack.append((testue,index))

        #if less or equal to most recent
        if testue <= stack[-1][0] and index != 0 :
            stack.append((testue,index))
        

        #if bigger than most recent/smallest
        elif testue > stack[-1][0]:

            while testue > stack[-1][0] and len(stack) > 0:
                ans[stack[-1][1]] = (index - stack[-1][1], 'possible')
                stack.pop()

                try: #if it is bigger than every testue in the stack, then go onto next round
                    stack[-1][0]
                
                except IndexError:
                    break

            stack.append((testue,index))

    for index, element in enumerate(ans):
        if type(element) != tuple:
            ans[index] = 'impossible'

    return ans
