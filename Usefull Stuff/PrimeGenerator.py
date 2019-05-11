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
    
getPrimes(100000)
