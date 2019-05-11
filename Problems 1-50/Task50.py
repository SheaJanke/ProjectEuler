# -*- coding: utf-8 -*-
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
    
getPrimes(1001000)
maxLength = 0
prime = 0
start = 0
while primeList[start] < 1000000:
    total = 0
    a = start
    while total < 1000000:
        total = total + primeList[a]
        if (a-start+1) > maxLength and total in primeList:
            prime = total
            maxLength = (a-start +1)
        a = a+1
    start = start + 1
print(prime)
print(maxLength)