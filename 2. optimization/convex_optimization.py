#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 12:57:06 2021

@author: q

Goal : Develop a Convex Optimization for a squared function

"""
# =============================================================================
# imports
# =============================================================================

# scientific computing
import numpy as np

# plotting
import matplotlib.pyplot as plt

# time
import time

# =============================================================================
# program test
# =============================================================================

if __name__ == '__main__':
    
    
    def func(x):
        return x ** 2
    
    def func_dx(x):
        return 2 * x
    
    
    x_axis = np.linspace(-2, 2, 100)
    y_axis = func(x_axis)
    
    plt.plot(x_axis, y_axis)
    plt.axhline( y = 0, color = 'black', linestyle = 'dashed')
    plt.axvline( x = 0, color = 'black', linestyle = 'dashed')
    plt.show()
    
    
    x = np.random.uniform(low = -0.25, high = 0.25, size = None) * 8
    y = func(x)
    
    learning_rate = 0.025
    epsilon = 0.005

    while np.abs(y) > epsilon:
    
        # get last update
        dx = func_dx(x)
        # update y
        y = y - (learning_rate * dx * np.sign(x))  
        # update x
        x = np.sign(x) * np.sqrt(y)
        
        # visualize updates
        plt.plot(x_axis, y_axis)
        plt.scatter( x , y, color = 'red')
        plt.axhline( y = 0, color = 'black', linestyle = 'dashed', lw = 1)
        plt.axvline( x = 0, color = 'black', linestyle = 'dashed', lw = 1)
        plt.show()
        plt.pause(0.001)
     
    print('Reached Convergence !!!') 

