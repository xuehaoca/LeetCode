class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        a = str(x)
        b = len(a)
        temp = str()
        temp1 = str()
        flag = 0
        if(a[0]== '-'):
            temp = temp + '-'
            flag = 1
        else:
            temp= temp + a[b-1]
        for i in range(1,b): 
            if(flag == 1):
                temp = temp + a[b-i]
            elif flag == 0:
                temp = temp + a[b-i-1]
        print temp
        if(temp[0] == 0):
            temp1 = temp[1:b]
        elif(temp[0]=='-' and temp[1]== '0'):
            temp1 = '-' + temp[2:b]
        else:
            temp1 = temp
        re = int(temp1)
        if(re > pow(2,31)-1 or re < -pow(2,31)):
            re = 0
        return re
        
                
