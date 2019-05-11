# -*- coding: utf-8 -*-
triangle = []
pentagon = []
hexagon = []

def generate (max):
    a = 1
    while a*(a+1)/2 < max:
        triangle.append(a*(a+1)/2)
        a = a+1
    a = 1
    while a*(3*a-1)/2 < max:
        pentagon.append(a*(3*a-1)/2)
        a = a+1
    a = 1
    while a*(2*a-1) < max:
        hexagon.append(a*(2*a-1))
        a = a+1


generate(100000000000)

same = set(triangle).intersection(pentagon)
same = set(same).intersection(hexagon)

print(same)