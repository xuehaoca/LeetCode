class Solution(object):
    def myAtoi(self, str1):
        """
        :type str: str
        :rtype: int
        """
        res = int()
        length = len(str1)
        flag = 1
        j = 0
        if(length == 0):
            return 0
        for i in range(0,len(str1)):
            if(str1[i] != ' '):
                j = i
                break
            else:
                continue
        print j
        if(str1[j] != '-' and (str1[j] < '0' or str1[j] > '9') and str1[j]!= '+'):
            return 0
        elif str1[j] == '-':
            flag = -1
            if(len(str1) == 1):
                return 0
        elif str1[j] == '+':
            flag = 1
            if(len(str1)== 1):
                return 0
        elif '0' < str1[j] < '9':
            res = res + (int)(str1[j])
            if(len(str1)== 1):
                return res
        for i in range(j+1,len(str1)):
            if(str1[i] < '0' or str1[i] > '9'):
                res = res * flag
                if(res > (pow(2,31)-1)):
                    res = pow(2,31)-1
                elif res < -1*pow(2,31):
                    res = -1*pow(2,31)
                return res
            res = res * 10 + int(str1[i])
        res = res * flag
        if(res > (pow(2,31)-1)):
            res = pow(2,31)-1
        elif res < -1*pow(2,31):
            res = -1*pow(2,31)
            return res
        return res
        
        
            
