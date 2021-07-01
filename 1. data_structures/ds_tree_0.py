#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 23:58:17 2021

@author: q

GOAL : Develop a binary tree implementation 

    - Tree Construction
    - Tree Traversal
    - Tree Insertion
    - Tree Search
    - Print Tree

"""

class Node():
    
    """ Binary Tree Node Class """
    
    def __init__(self, value):
        """ value, left, right """
        self.value = value
        self.left = None
        self.right = None
    

    def insert(self, value):
        """ Insert value in an empty space,
        n < value, to the left """
        if self.value:
            
            if value < self.value:
                
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
                    
            elif value > self.value:
                
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)
        else:
            
            self.value = value

        pass
    
    def search(self, value):
        """ Search - Recursive Solution """
        
        if value < self.value:
            
            if self.left is None:
                return str(value)+" : not Found !"
            return self.left.search(value)
        
        elif value > self.value:
            
            if self.right is None:
                return str(value)+" : not Found !"
            return self.right.search(value)
        
        else:
            return str(self.value) + " : Found !"


    def inorder(self):
        """ InOrder L-value-R Print """
        
        if self.left:
            self.left.inorder()
            
        print(self.value)
        
        if self.right:
            self.right.inorder()    

    def preorder(self):
        """ PreOrder value-L-R Print """
        
        print(self.value)
        
        if self.left:
            self.left.preorder()
        
        if self.right:
            self.right.preorder()    


    def postorder(self):
        """ PostOrder L-R-value Print """
        
        if self.left:
            self.left.postorder()
        
        if self.right:
            self.right.postorder()    
        
        print(self.value)


if __name__ == '__main__':

    """ Binary Tree Implementation """    

    wisdom = Node(10)
    
    for n in [9, 8, 10, 12, 11, 15, 14]:
        wisdom.insert(n)
    
    print(wisdom.search(n))

    wisdom.postorder()