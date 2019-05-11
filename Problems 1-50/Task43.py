# -*- coding: utf-8 -*-
import time 
startTime = time.time()

sum = 0
works = []
m2 = []
m7 = []
m17 = []
possible = []

def addZero (num):
    final = ""
    for a in range(0,3-len(num)):
        final += "0"
    final += num
    return final

def pandigital(num):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    for place in num:
        if place not in digits:
            return False
        else:
            digits.remove(place)
    return True

def lastNum(num):
    digits = ["0","1","2","3","4","5","6","7","8","9"]
    for place in num:
        digits.remove(place)
    if(digits[0]!= "0"):
        possible.append(digits[0] + num)

def check(num):
    if(int(num[2:5])% 3 != 0):
        return False
    if(int(num[3:6])% 5 != 0):
        return False
    if(int(num[5:8])% 11 != 0):
        return False
    if(int(num[6:9])% 13 != 0):
        return False
    return True

for a in range(0,1000,2):
    hold = str(a)
    if(len(hold)<3):
       hold = addZero(hold)
    if pandigital(hold) == True:
        m2.append(hold)
    
for a in range(0,1000,7):
    hold = str(a)
    if(len(hold)<3):
       hold = addZero(hold)
    if pandigital(hold) == True:
        m7.append(hold)

for a in range(0,1000,17):
    hold = str(a)
    if(len(hold)<3):
       hold = addZero(hold)
    if pandigital(hold) == True:
        m17.append(hold) 

for a in m2:
    for b in m7:
        if pandigital(a + b) == True:
            for c in m17:
                if pandigital(a + b + c) == True:
                    lastNum(a + b + c)
for a in possible:
    if check(a) == True:
        works.append(a)
                
for a in works:
    sum += int(a)

print(sum)    
print(time.time() - startTime)  
    