#Date: April 2, 2021
#Purpose: Waterloo's gr 12 weekly math problem (emailed on april 1, 2021)

import math

ans = 0
prime = []
table = []

def primeTable(x):

    global table
    
    count = 0

    #finding all prime numbers from 3 to x
    for num in range(2,x): 
        
        for factor in range(num + 1, int(math.sqrt(num))):
            if num % factor == 0:
                count += 1

        if count == 0:
            table.append(num)
    

def primeFactors(n):

    global table
    global prime
    
    prime = []
    
    #all the 2s that are divisible into n
    while n % 2 == 0:
        prime.append(2)
        n = n / 2
          
    # n must be odd at this point
    # try all non-two prime factors into n until n's square root
    for i in table:
          
        #if i is factorable into n, keep trying it until it cant factor anymore
        while n % i == 0:
            prime.append(i)   
            n = n / i
              
    # ** special condition in case n is a prime (n itself wont be included in 3 to its square root)
    # number greater than 2 or else the first while loop would have caught it
    if n > 2:
        prime.append(i)

    return prime


primeTable(100) #the largest prime number we will need is up to sqrt(100000) = around 100
    
for num in range(10000,100000):

    primeFactors(num)
    
    if str(num)[0] == str(num)[3] and str(num)[1] == str(num)[4] and str(num)[2] == '0'  and all(i % 2 == 1 for i in prime) and len(prime) == 5:

        check_l = []
        check = 0
        
        for x in prime:
            if x in check_l:
                check += 1
            check_l.append(x)

        if check == 0:
            ans += 1

print(ans)

    return prime


primeTable(100) #the largest prime number we will need is up to sqrt(100000) = around 100
    
for num in range(10000,100000):

    primeFactors(num)
    
    if str(num)[0] == str(num)[3] and str(num)[1] == str(num)[4] and str(num)[2] == '0'  and prime == 5:
        ans += 1

print(ans)

    
