#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Sat May 29 09:30:09 2021

@author: q

GOAL : Yield all possible binary combinations from a set

"""


items = [1, 2, 3]


def powerSet(items):
    
    """
    
    Yield all possible combinations in a Set
    
    """
    
    N = len(items)
    
    print([bin(x)[2:] for x in range(N)])
    btotal = []
    ctotal = []
    # enumerate the 2**N+1 possible combinations 
    for i in range(2**N):
        binary = []
        combo = []    
        for j in range(N):
            # test bit jth of integer i
            print(i, bin(i), j, bin(j), i >> j, bin(i>>j))
            binary.append(bin(i >> j)[2:])
            
            if (i >> j) % 2 == 0:
                
                combo.append(items[j])
        
        btotal.append(binary)
        ctotal.append(combo)
        
    return btotal, ctotal

b, t = powerSet(items)

print(b)

print(t)
    
"""

About the combination sequence

1. The domain in binary items the range in len(items)

    for list if 4 elements : ['0', '1', '10', '11']
    
2. The domain if the possible combinations : 2**N

    2**N always yields an even number
        The range for 2**N, start with zero and ends with an even number
        
3. First and last combination :
    
    first = i is bin 0, j is dec 0, i >> j % 2 == 1,
            the rest elements are %2 == 0
            
    last = 

4. Combo is empty the first loop

"""
