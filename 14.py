# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:49:37 2017

@author: Elani
"""

#14. Longest Common Prefix
class Solution(object):
    def findCommonPrefix(self,s1,s2):
        #from tail to head
        if s1=='' or s2=='':
            return ''
        for i in xrange(len(s1),0,-1):
            if s1[0:i] == s2[0:i]:
                return s1[0:i]
           
        return ''
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        #Notice:strs maybe an empty list
        if len(strs)==0:
            return ''
        elif len(strs) == 1:
            return strs[0]
        else:
            common_prefix = strs[0]
            for str in strs[1:]:
                common_prefix = self.findCommonPrefix(common_prefix,str)
            return common_prefix
    
"""            
strs=['aa','ab']
solu = Solution()
prefix = solu.longestCommonPrefix(strs)
print prefix
"""

"""
class Solution:

    def lcp(self, str1, str2):
        i = 0
        while (i < len(str1) and i < len(str2)):
            if str1[i] == str2[i]:
                i = i+1
            else:
                break
        return str1[:i]

    # @return a string                                                                                                                                                          
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp,strs)
"""
"""
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        #zip(*strs) :[('a', 'a', 'a'), ('a', 'b', 'b')]    
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)
"""
"""
#C solution
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        for(int idx=0; strs.size()>0; prefix+=strs[0][idx], idx++)
            for(int i=0; i<strs.size(); i++)
                if(idx >= strs[i].size() ||(i > 0 && strs[i][idx] != strs[i-1][idx]))
                    return prefix;
        return prefix;
    }
};
"""