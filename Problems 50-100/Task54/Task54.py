# -*- coding: utf-8 -*- 
import time
start = time.time()
from collections import Counter
file = open("pokerhands.txt","r")
def hands(string):
    global h1
    global h2
    combined = string.split()
    h1 = combined[0:5]
    h2 = combined[5:len(string)]

def flush(hand):

    for a in range(1,5):
        if hand[0][1] == hand[a][1]: 
            continue
        else:
            return 0
    hand = toNumbers(hand)
    hand.sort()
    return hand[4]

def straight(hand):
    num = []
    for a in hand:
        if a[0] == "J":
            num.append(11)
        elif a[0] == "Q":
            num.append(12)
        elif a[0] == "K":
            num.append(13)
        elif a[0] == "A":
            num.append(14)
        elif a[0] == "T":
            num.append(10)
        else:
            num.append(int(a[0]))
            
    num.sort()
    for a in range(0,4):
        if num[a+1] == num[a] +1:
            continue
        else:
            return 0
    return num[4]
    

def four(hand):
    num = []
    hand = toNumbers(hand)
    for a in hand:
        num.append(a)
    count = Counter(num)
    if count.most_common(1)[0][1] == 4:
        return count.most_common(1)[0][0]
    else:
        return 0

def fullHouse(hand):
    num = []
    hand = toNumbers(hand)
    for a in hand:
        num.append(a)
    count = Counter(num)
    if count.most_common(2)[0][1] == 3 and count.most_common(2)[1][1] == 2:
        return count.most_common(1)[0][0]
    else:
        return 0
    
def three(hand):
    num = []
    hand = toNumbers(hand)
    for a in hand:
        num.append(a)
    count = Counter(num)
    if count.most_common(1)[0][1] == 3:
        return count.most_common(1)[0][0]
    else:
        return 0
def pair(hand):
    num = []
    hand = toNumbers(hand)
    for a in hand:
        num.append(a)
    count = Counter(num)
    if count.most_common(1)[0][1] == 2:
        return count.most_common(1)[0][0]
    else:
        return 0
    
def twoPair(hand):
    num = []
    hand = toNumbers(hand)
    for a in hand:
        num.append(a)
    num.sort()
    count = Counter(num)
    if count.most_common(2)[0][1] == 2 and count.most_common(2)[1][1] == 2:
        return count.most_common(2)[1][0]
    else:
        return 0
def toNumbers(hand):
     hand1 = []
     for a in hand:
        if a[0] == "J":
            hand1.append(11)
        elif a[0] == "Q":
            hand1.append(12)
        elif a[0] == "K":
            hand1.append(13)
        elif a[0] == "A":
            hand1.append(14)
        elif a[0] == "T":
            hand1.append(10)
        else:
            hand1.append(int(a[0]))
     return hand1

def royalFlush(hand):
    if flush(hand) > 0 and straight(hand) == 14:
        return 1
    else:
        return 0
def straightFlush(hand):
    if flush(hand) > 0 and straight(hand) > 0:
        return straight(hand)
    else:
        return 0

def highest(h1,h2):
    hand1 = []
    hand2 = []
    for a in h1:
        if a[0] == "J":
            hand1.append(11)
        elif a[0] == "Q":
            hand1.append(12)
        elif a[0] == "K":
            hand1.append(13)
        elif a[0] == "A":
            hand1.append(14)
        elif a[0] == "T":
            hand1.append(10)
        else:
            hand1.append(int(a[0]))
    for a in h2:
        if a[0] == "J":
            hand2.append(11)
        elif a[0] == "Q":
            hand2.append(12)
        elif a[0] == "K":
            hand2.append(13)
        elif a[0] == "A":
            hand2.append(14)
        elif a[0] == "T":
            hand2.append(10)
        else:
            hand2.append(int(a[0]))
    hand1.sort()
    hand2.sort()
    for a in range(0,5):
        if hand1[4-a] > hand2[4-a]:
            return "h1"
        elif hand1[4-a] < hand2[4-a]:
            return "h2"
    
def wins(h1,h2):
    if royalFlush(h1) > royalFlush(h2):
        return True
    elif royalFlush(h2) > royalFlush(h1):
        return False
    elif royalFlush(h1) > 0:
        if highest(h1,h2) == "h1":
            return True
    else:
        if straightFlush(h1) > straightFlush(h2):
            return True
        elif straightFlush(h2) > straightFlush(h1):
            return False
        elif straightFlush(h1) > 0:
            if highest(h1,h2) == "h1":
                return True
        else:
            if four(h1) > four(h2):
                return True
            elif four(h2) > four(h1):
                return False
            elif four(h1) > 0:
                if highest(h1,h2) == "h1":
                    return True
            else:
                if fullHouse(h1) > fullHouse(h2):
                    return True
                elif fullHouse(h2) > fullHouse(h1):
                    return False
                elif fullHouse(h1) > 0:
                    if highest(h1,h2) == "h1":
                        return True
                else: 
                    if flush(h1) > flush(h2):
                        return True
                    elif flush(h2) > flush(h1):
                        return False
                    elif flush(h1) > 0:
                        if highest(h1,h2) == "h1":
                            return True
                    else:
                        if straight(h1) > straight(h2):
                            return True
                        elif straight(h2) > straight(h1):
                            return False
                        elif straight(h1) > 0:
                            if highest(h1,h2) == "h1":
                                return True
                        else:
                            if three(h1) > three(h2):
                                return True
                            elif three(h2) > three(h1):
                                return False
                            elif three(h1) > 0:
                                if highest(h1,h2) == "h1":
                                    return True
                            else:
                                if twoPair(h1) > twoPair(h2):
                                    return True
                                elif twoPair(h2) > twoPair(h1):
                                    return False
                                elif twoPair(h1) > 0:
                                    if highest(h1,h2) == "h1":
                                        return True
                                else:
                                    if pair(h1) > pair(h2):
                                        return True
                                    elif pair(h2) > pair(h1):
                                        return False
                                    elif pair(h1) > 0:
                                        if highest(h1,h2) == "h1":
                                            return True
                                    else:
                                        if highest(h1,h2) == "h1":
                                            return True
                                        else:
                                            return False
win = 0
for a in range(0,1000):                                       
    hands(file.readline())
    if wins(h1,h2) == True:
        win = win +1
print(win)
print(time.time()-start)
            







