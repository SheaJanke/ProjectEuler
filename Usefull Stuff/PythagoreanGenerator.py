# -*- coding: utf-8 -*-
identities = []

def smallerThan (num):
    n = 2
    while n**2 < num:
        for m in range(1,n):
            if n**2 + m**2 < num:  
                a = n**2 - m**2
                b = 2 * n * m
                c = n**2 + m**2
                identities.append([a,b,c])
        n+=1        

smallerThan(50)
print(identities)