# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 15:42:12 2017

@author: Elani
"""
#9. Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        else:
            l = len(str(x))
            print l
            for i in xrange(1,l/2+1):
                #compare the head and the tail
                x1 = x%(10**(l-i+1)) /(10**(l-i))
                x2 = x%(10**i) /(10**(i-1))
                print x1
                print x2
                if x1!=x2 :
                    return False
              
        return True
        
"""
public boolean isPalindrome(int x) {
    if (x<0 || (x!=0 && x%10==0)) return false;
    int rev = 0;
    while (x>rev){
    	rev = rev*10 + x%10;
    	x = x/10;
    }
    return (x==rev || x==rev/10);
}
"""