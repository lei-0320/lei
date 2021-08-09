#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 14:09:58 2021

@author: apple
"""

import numpy as np
from scipy.linalg import solve
A=np.array([[0.5,0.2],[1,1]])
B=np.array([10,30])
x=solve(A,B)
print(x)

"""
for this problem solving, we could assume that:
    we will produce x vanila ice cream and y strawberry ice cream.
    the object: Max_profits=2x+3y
    the constrains: 0.5x+0.2y<=10
                    x+y>=30
                    x & y >0
so that, we could get the answer x~=13 , y~=17. but as i find ,the price for
 strawberry is $3 each. if we wanna get the max profits, we should produce only
strawberry ice cream,and the we should produce 0 vanila ice cream and 50 strawberry
ice cream. the Max_profits would be $150.
"""