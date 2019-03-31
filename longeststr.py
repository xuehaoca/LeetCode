class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = len(s)
        m = 0
        n = 1
        if(len(s) == 0):
            return 0
        for i in range(1, a):
            for j in range (m, i):
                if( s[j] == s[i]):
                    m = j + 1
            if((i - m + 1) > n):
                n = i - m + 1
            i = i + 1
        return n
            
