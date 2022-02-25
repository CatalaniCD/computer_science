#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:52:20 2021

@author: q

GOAL : from binary_tree to taken_not_taken knapsack

"""


def binary_tree(levels = 3):
    binary = '01'
    L = len(binary)
    
    tree = []
    for i in range( L ** levels):
        leaf = ''
        for j in range(levels):
            # print(i, j, L, (L ** j),  i // (L ** j), i // (L ** j) % L)
            leaf += binary[i // (L ** j) % L]
        # print()    
        tree += [leaf]
    
    return tree

print(binary_tree())

def index_taken_notTaken(levels = 2):
    binary = '10'
    L = len(binary)
    
    tree = []
    for i in range( L ** levels):
        leaf = ''
        for j in range(levels):
            
            # print(i, j, L, (L ** j),  i // (L ** j), i // (L ** j) % L)
            leaf += binary[i // (L ** j) % L]
        
        # print()    
        taken = []
        for l in range(len(leaf)):
            
            if leaf[l] == '1':
                taken += [l]

        tree += [taken]
    return tree

items = ['dog', 'cat', 'chipmunk']
index = index_taken_notTaken(levels = len(items))
print(index)
