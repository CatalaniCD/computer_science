#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Sat May 29 10:52:20 2021

@author: q

GOAL : from binary_tree to n possible combinations in a set 
        
        - combinatorial optimization : knapsack problem

source : 
    
    - https://en.wikipedia.org/wiki/Knapsack_problem
    - https://en.wikipedia.org/wiki/Combinations
    - https://en.wikipedia.org/wiki/Power_set

"""


# =============================================================================
# Functions
# =============================================================================

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


def index_taken_notTaken(items_list = []):
    
    """
    Input :
        
        * levels : default = 3, number of levels for a binary tree
        
    Returns :
        
        * len(list) ** levels possible combinations for a list
        
    """
    
    binary = '10'
    L = len(binary)
    levels = len(items_list)
    
    tree = []
    for i in range( L ** levels):
        leaf = ''
        for j in range(levels):
            
            leaf += binary[i // (L ** j) % L]
        
        # print()    
        taken = []
        for l in range(len(leaf)):
            
            if leaf[l] == '1':
                taken += [items_list[l]]

        tree += [taken]
    return tree

if __name__ == '__main__':

    print(f'\n=== Binary Tree Combinations ===\n\n{binary_tree()}\n')
    
    pets = ['dog', 'cat', 'chipmunk']
    index = index_taken_notTaken( items_list = pets )
    print(f'\n=== nCr combinations for pets list ===\n\n{index}\n')


        
