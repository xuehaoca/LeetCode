class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        c1 = True
        c2 = False
        lie1 = 0
        lie2 = 0
        count1 = 0
        count2 = 0
        i = len(s)
        s1 = str()
        s2 = str()
        # numRows > 3 get the two array s1 s2
        for j in range(0,i):
            if( c1 == True):
                s1 = s1 + s[j]
                count1 = count1 + 1
                if(count1 == numRows):
                    count1 = 0
                    c1 = False
                    c2 = True
                    lie1 = lie1 + 1
            elif( c2 == True):
                s2 = s2 + s[j]
                count2 = count2 + 1
                if(count2 == (numRows - 2)):
                    count2 = 0
                    c1 = True
                    c2 = False
                    lie2 = lie2 + 1
        if(count1 != 0): lie1 = lie1 + 1
        if(count2 != 0): lie2 = lie2 + 1   
        ss1 = len(s1)
        ss2 = len(s2)
        j = 0
        s3 = str()
        c1 = True
        c2 = False
        #special condition numRows == 2
        if(numRows == 2):
            for i in range(0,len(s)):
                if(2*i >= len(s)): 
                    break
                s3 = s3 + s[2*i]
            for i in range(0,len(s)):
                if((2*i + 1) >= len(s)): 
                    break
                s3 = s3 + s[2*i+1]
            return s3
        #print the first line
        while(j < ss1):
            s3 = s3 + s1[j]
            j = j + numRows
        c1 = True
        c2 = False
        k1 = k2 = 0
        if(len(s) <= numRows):
            return s
        if(numRows == 1):
            return s
        print lie1,lie2
        print s1,s2,s3
        #print the middle lines
        for j in range(1,numRows-1):
            for k in range(0,lie1+lie2):
                if( c1 == True):
                    if((j + k1 * numRows) > (len(s1)-1)):
                        break
                    s3 = s3 + s1[j + k1 * numRows]
                    k1 = k1 + 1
                    c1 = False
                    c2 = True
                    
                elif( c2 == True):
                    if((numRows-2-j + k2*(numRows-2)) > (len(s2)-1)):
                        break
                    s3 = s3 + s2[numRows-2-j + k2*(numRows-2)]
                    k2 = k2 + 1
                    c1 = True
                    c2 = False
            c1 = True
            c2 = False
            k1 = 0
            k2 = 0
        j = numRows-1
        #print the last line
        while(j < ss1):
            s3 = s3 + s1[j]
            j = j + numRows
            
        return s3
