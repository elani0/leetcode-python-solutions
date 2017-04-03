# -*- coding: utf-8 -*-
"""
Created on Mon Apr 03 15:03:08 2017

@author: Elani
"""
#155. Min Stack

'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.stack:
            self.stack.append(x)
            self.min.append(x)
        else:
            if x < self.min[-1]:
                self.min.append(x)
            else:
                self.min.append(self.min[-1])
            self.stack.append(x)


    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return None
        self.stack.pop()
        self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    #must in O(1),so traversing is ineffective .
    def getMin(self):
        """
        :rtype: int
        """
        if not self.min:
            return None
        else:
            return self.min[-1]