class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        maxLen=0
        pal = [[ 0 for i in range(n)] for i in range(n)]
        for i in range(0,n):
            j=i
            while (j>=0):
                if (s[j]==s[i] and (i-j<2 or pal[j+1][i-1])):
                    pal[j][i]=True
                    if((i-j+1) >= maxLen):
                        str1 = s[j:i+1]
                    maxLen= max(maxLen, i-j+1)
                j = j - 1
        return str1
