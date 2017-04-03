# -*- coding: utf-8 -*-
"""
Created on Sun Apr 02 12:05:41 2017

@author: Elani
"""
#38. Count and Say
"""
The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.
"""
'''
import re
#s = ''.join(str(len(group)) + digit
s='1'
for group, digit in re.findall(r'((.)\2*)', s):
    print digit
'''
'''
Solution 1 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
    return s
'''
'''
Solution 2 ... using a regular expression

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(group)) + digit
                    for group, digit in re.findall(r'((.)\2*)', s))
    return s
'''
'''
Solution 3 ... using groupby

def countAndSay(self, n):
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + digit
                    for digit, group in itertools.groupby(s))
    return s
'''

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        if n == 1:
            return '1'
        l=['1']
        while(len(l)) < n:
            s=l[-1]
            chars = set(list(s))
            count = {}
            for c in chars:
                count[c] = 0
            encode = ''
            pre_c = s[0]
            count[s[0]] += 1
            for char in s[1:]:
                if char != pre_c:
                    encode += str(count[pre_c])+pre_c
                    count[pre_c] = 0
                count[char] += 1
                pre_c = char
            for char in chars:
                if count[char] != 0:
                    encode += str(count[char])+char
            l.append(encode)
        return l[-1]

s = Solution()
print s.countAndSay(6)  
         