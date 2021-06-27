#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 29 10:52:20 2021

@author: q

GOAL : from binary_tree to n possible combinations in a set (taken_not_taken knapsack)

"""


def binary_tree(levels = 3):
    
    """ 
    Input : 
        
        * levels : default = 3, number of levels for a binary tree
        
    Returns :
        
        * list of binary leafs and ancestors
    """
        
    binary = '01'
    L = len(binary)
    
    tree = []
    # iterate in the number total leafs
    for i in range( L ** levels):
        leaf = ''
        # iterate in the number of elements for each leafs
        for j in range(levels):
            leaf += binary[i // (L ** j) % L]
        # print()    
        tree += [leaf]
    
    return tree

print(binary_tree())

def index_taken_notTaken(levels = 2, items = []):
    
    """
    Input :
        
        * levels : default = 3, number of levels for a binary tree
        
    Returns :
        
        * len(list) ** levels possible combinations for a list
        
    """
    
    binary = '10'
    L = len(binary)
    
    tree = []
    for i in range( L ** levels):
        leaf = ''
        for j in range(levels):
            
            leaf += binary[i // (L ** j) % L]
        
        # print()    
        taken = []
        for l in range(len(leaf)):
            
            if leaf[l] == '1':
                taken += [items[l]]

        tree += [taken]
    return tree

items = ['dog', 'cat', 'chipmunk']
index = index_taken_notTaken(levels = len(items), items = items)
print(index)


        