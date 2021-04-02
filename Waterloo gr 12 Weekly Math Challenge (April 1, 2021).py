#Date: April 2, 2021
#Purpose: Waterloo's gr 12 weekly math problem (emailed on april 1, 2021)

import math

ans = 0
prime = 0

def primeFactors(n):
    
    global prime
    prime = 0
    
    #all the 2s that are divisible into n
    while n % 2 == 0:
        prime += 1
        n = n / 2
          
    # n must be odd at this point
    # try all odd factors into n until n's square root
    for i in range(3,int(math.sqrt(n))+1,2):
          
        #if i is factorable into n, keep trying it until it cant factor anymore
        while n % i == 0:
            prime += 1
            n = n / i
              
    # ** special condition in case n is a prime (n itself wont be included in 3 to its square root)
    # number greater than 2 or else the first while loop would have caught it
    if n > 2:
        prime += 1

    return prime


for num in range(10000,100000):
    
    primeFactors(num)
    
    if str(num)[0] == str(num)[3] and str(num)[1] == str(num)[4] and str(num)[2] == '0'  and prime == 5:
        ans += 1

print(ans)


    
