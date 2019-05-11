# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 10:29:47 2019

@author: Shea
"""
palindromes = [];
    
def reverse(num):
    string = str(num)
    newNum = ""
    for a in range(0,len(string)):
        newNum += string[len(string) - (a+1)]
    return int(newNum)   
 
def binary(num): 
    string = str(num)
    newNum = ""
    for a in range(0,len(string)):
        newNum += string[len(string) - (a+1)]
    y = bin(int(newNum))[2:]
    return int(y)
    

for a in range(1,1000000):
   if reverse(a) == a:
       if reverse(binary(a)) == binary(a):
           palindromes.append(a)   
total = 0
for a in palindromes:
    total += a
print(total)