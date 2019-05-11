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
    

def works(start, increase):
    if (start + increase) in primeList and (start + 2*increase) in primeList:
        if permutations(start, start+increase) == True and permutations(start, start+2*increase) == True:
            print(str(start) + "" + str(start + increase) + "" + str(start + 2*increase))
def permutations(num1, num2):
    digits1 = []
    digits2 = []
    for number in str(num1):
        digits1.append(int(number))
    for number in str(num2):
        digits2.append(int(number))
    digits1.sort()
    digits2.sort()
    if(digits1 == digits2):
        return True

getPrimes(10000) 

for primes in primeList:
    for second in primeList:
        if permutations(primes,second) == True and primes != second:
            works(primes,second-primes)