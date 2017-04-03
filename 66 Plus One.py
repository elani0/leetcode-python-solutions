# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 15:19:59 2017

@author: Elani
"""
#66. Plus One
def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]