count = 0
for x in range(1,1000000000):
    count = 0
    for y in range(1,x + 1):
        if x / y == x // y:
            count += y
    if count / x == 2:
        print(x)
        
