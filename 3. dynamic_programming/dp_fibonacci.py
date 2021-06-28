#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 11:06:10 2021

@author: q

Goal : Study Dynamic Programming Concepts for CGA Exam

Study Case : Fibonacci Numbers

    - Binary Recursion
    
    - Top-Down with Memoization
    
    - Bottom-Up with Tabualtion
    
"""


def fiboRecursive(n):
    """ Fibonacci numbers solved with binary recursion """    
    if n == 0 or n == 1:
        return 1
    else:
        return fiboRecursive(n - 1) + fiboRecursive(n - 2)

num = 15
print(f'{num} fiboRecur number is : ', fiboRecursive(num))
    

def tabFibo(n):
    """ Fibonacci numbers solved with tabulation """
    base = [1, 1]
    for i in range(2, n + 1):
        base.append(base[i - 1] + base[i - 2])
    return base[n]

print(f'{num} tabFibo   number is : ', tabFibo(num))
    
def memoFib(n, memo = {}):
    """ Fibonacci numbers solved with memoization using dictionary"""    
    if n == 0 or n == 1:
        return 1
    
    try:    
        return memo[n]
    except KeyError:
        result = memoFib(n-1, memo) + memoFib(n-2, memo)
        memo[n] = result
        return result

print(f'{num} memoFibo dict number is : ', memoFib(num))


def lmemoFib(n, memoize):
    """ Fibonacci numbers solved with memoization using list"""    
    if n < 3:
        return n
    if memoize[n] >= 0:
        return memoize[n]
    else:
        memoize[n] = lmemoFib(n-1, memoize) + lmemoFib(n-2, memoize)
        return memoize[n]

def wrapperFib(n):
    """ wrapper function for memoFib usign list """
    memoize = [ -1 for x in range(n+1) ]
    return lmemoFib(n, memoize)


print(f'{num} memoFibo dict number is : ', wrapperFib(num))
