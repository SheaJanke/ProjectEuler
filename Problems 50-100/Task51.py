# -*- coding: utf-8 -*-
from collections import Counter
import time
start = time.time()
primeList = []

def getPrimes(max):
    primes = []
    for a in range(2,max+1):
        primes.append(True)
    for a in range(0,int(max/2)):
        if primes[a] == True:
            for b in range (2*a + 2, max-1,a+2):
                primes[b] = False
    for a in range(2,max+1):
        if primes[a-2] == True:
            primeList.append(a)
    
getPrimes(1000000)
primeList = list(map(str,primeList))

global stars
stars = [0,0,0,0,0,0,0]
def next(digit):
    if stars[digit] == 0:
        stars[digit] = 1
    elif digit < len(stars)-1:
        stars[digit] = 0
        next(digit+1)


while stars[len(stars)-1] == 0:
    next(0)
    hold = []
    works= [0]
    for num in primeList:
        number = num
        replace = "10"
        finish = True
        for a in range(0,len(stars)):
            if stars[a] == 1 and len(number) > a and a == 0:
                replace = number[len(number)-1]
                number = number[:len(number)-(a+1)] + "*" 
            elif stars[a] == 1 and len(number) > a:
                if replace == "10":
                    replace = number[len(number)- (a+1)]
                    number = number[:len(number)-(a+1)] + "*" + number[len(number)-a:]
                elif number[len(number)-(a+1)] == replace:
                    number = number[:len(number)-(a+1)] + "*" + number[len(number)-a:]
                else:
                    finish = False
        if finish == True:
            hold.append(number)
    data = Counter(hold)
    if data.most_common(1)[0][1] == 8:
        print(data.most_common(1))
        break
print(time.time() - start)