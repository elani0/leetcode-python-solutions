# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:43:04 2016

@author: Elani
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        #TLE
        l=['a','e','i','o','u']
        index=[]
        for i in xrange(len(s)):
            if s[i].lower() in l:
                index.append(i)

        for i in xrange(len(index)/2):
            char2 = s[index[i]]
            char1 = s[index[-(i+1)]]
            s=s[:index[i]] + char1 + s[index[i]+1:index[-(i+1)]] + char2 +s[index[-(i+1)]+1:]
        
        return s
        """
        chars=[s[i] for i in xrange(len(s))]
        l = ['a','e','i','o','u']
        index=[]
        for i in xrange(len(s)):
            if s[i].lower() in l:
                index.append(i)
        for i in xrange(len(index)/2):
            chars[index[i]],chars[index[-(i+1)]] = chars[index[-(i+1)]],chars[index[i]]
        r = ''.join(chars)  
        
        return r
"""
#alt1
def reverseVowels(self, s):
    vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
    return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)
"""            


"""
#alt2
def reverseVowels(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
"""                
        
if __name__ =="__main__":
    s = Solution()
    rs = s.reverseVowels('leetcode')
    print rs
    