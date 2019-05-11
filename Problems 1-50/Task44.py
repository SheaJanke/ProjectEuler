# -*- coding: utf-8 -*-
terms = []
min = 10000000000
max = 10000000

def getTerms(max):
    n = 1;
    while (n*(n+2))/2 <= max:
        terms.append(int((n*(3*n-1))/2))
        n = n+1

def works (num1, num2):
    global min
    hold = num1+num2
    if hold in terms:
        hold = num1-num2
        if hold in terms:
            min = hold


getTerms(max)
a = 0
b = 1
while a < len(terms)-1:   
    while terms[b] - terms[a] < min:
        works(terms[b], terms[a])
        if b < len(terms)-1:
            b = b+1
        else:
            break
    a = a+1
    b = a+1


print(min)