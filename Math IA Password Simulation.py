#Name: Terry Su
#Date: December 6, 2020
#Purpose: Mathematics SL: IA Exploration
#         - Password Generation Simulation

import random

#Initialization

Passwords = []
count = 0
Share = []

#Password Algorithm

for x in range(0,100):
    Passwords.append(str(random.randint(1,4)) + \
                     str(random.randint(1,4)) + \
                     str(random.randint(1,4)) + \
                     str(random.randint(1,4)))

print(Passwords)
print()

#Verifying for Password Repitition

for x in Passwords:
    Passwords2 = Passwords
    Passwords2.pop(count)
    count += 1
    for y in Passwords2:
        if x == y:
            Share.append(x)
           
Share = list(dict.fromkeys(Share)) #removes any duplicates in Share (ex: if 3 students share 1 password)


for x in Share:
    print('2 or more students share the password: ' + x)


