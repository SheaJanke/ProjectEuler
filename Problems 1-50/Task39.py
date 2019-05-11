# -*- coding: utf-8 -*-
perimeter = []
triples = []

def smallerThan (num):
    n = 2
    while n**2 < num:
        for m in range(1,n):
            if n**2 + m**2 < num:  
                a = n**2 - m**2
                b = 2 * n * m
                c = n**2 + m**2
                x = a
                y = b
                z = c
                while a + b + c <= num:    
                    if [a,b,c] not in triples:  
                        triples.append([a,b,c])
                        perimeter.append(a+b+c)
                        a+=x
                        b+=y
                        c+=z
                    else:
                        break
                    
        n+=1        

smallerThan(1000)
max = 0
answer = 0
for num in perimeter:
    if perimeter.count(num) > max:
        max = perimeter.count(num)
        answer = num
print(answer)
print(perimeter.count(120))