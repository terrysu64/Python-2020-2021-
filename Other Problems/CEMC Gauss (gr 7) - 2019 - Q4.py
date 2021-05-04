arr = [(20,19)]
curr = []

def expand():
    global curr
    global arr
    curr = []
    
    for index,coord in enumerate(arr):

        if type(coord) == tuple:
            if x == 1:
                curr.append((coord[0] + x, coord[1],'h'))
                curr.append((coord[0] - x, coord[1],'h'))
                curr.append((coord[0], coord[1] + x,'v'))
                curr.append((coord[0], coord[1] - x,'v'))
                arr[index] = str(arr[index])

            elif coord[2] == 'h':
                curr.append((coord[0], coord[1] + x,'v'))
                curr.append((coord[0], coord[1] - x,'v'))
                arr[index] = str(arr[index])

            elif coord[2] == 'v':
                curr.append((coord[0] + x, coord[1],'h'))
                curr.append((coord[0] - x, coord[1],'h'))
                arr[index] = str(arr[index])

    for y in curr:
        arr.append(y)

def analyze():
    
    global curr
    left = ['','','','','']
    
    for z in curr:
        if z[0] == 27 and z[1] == 33:
            left[0] = 'y'

        elif z[0] == 30 and z[1] == 40:
            left[1] = 'y'

        elif z[0] == 21 and z[1] == 21:
            left[2] = 'y'

        elif z[0] == 42 and z[1] == 44:
            left[3] = 'y'

        elif z[0] == 37 and z[1] == 37:
            left[4] = 'y'

    return left

for x in range(1,11):
    expand()

ans = analyze()
print(ans)




        
        
