# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:48:31 2016

@author: Elani
"""

class Solution(object):
    def canWinNim(self,n):
        """
        :type n: int
        :rtype: bool
        """
        '''
        #Runtime Error:Line 8: RuntimeError: maximum recursion depth exceeded in cmp
        win_l=[1,2,3]
        if n in win_l:
            return True
        else:
            for i in xrange(1,3,1):
                if self.canWinNim(n-i)==0:
                    return True
            else:
                return False
        '''
        return n % 4 > 0
        
                
if __name__ == "__main__":
    s=Solution()
    re=s.canWinNim(5)
    print re

'''
def fac(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
        
if __name__ == "__main__":
    print fac(3)
'''