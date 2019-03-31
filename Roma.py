class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i1 = num - (num//10)*10
        i2 = num - (num//100)*100-i1
        i3 = num - (num//1000)*1000-i2-i1
        i4 = num - i3-i2-i1
        flag1 = 0
        flag2 = 0
        flag3 = 0
        flag4 = 0
        i2 = i2 / 10
        i3 = i3 / 100
        i4 = i4 / 1000
        
        if(5<i4<9):
            flag4 = 1
            i4 = i4 -5
        if(5<i3<9):
            flag3 = 1
            i3 = i3 - 5
        if(5<i2<9):
            flag2 = 1
            i2 = i2 -5
        if(5<i1<9):
            flag1 = 1
            i1 = i1 - 5
        result = str()
        for i in range(0,i4):
            if(i4 == 0):
                break
            elif(i4 <= 3 ):
                result = result + 'M'
            elif(i4 == 4):
                return 0
            elif(i4 == 5):
                return 0
            elif(i4 == 9):
                return 0
        for i in range(0,i3):
            if(flag3 == 1):
                result = result + 'D'
                flag3 = 0
            if(i3 == 0):
                break
            elif(i3 <= 3 ):
                result = result + 'C'
            elif(i3 == 4):
                result = result + 'CD'
                break
            elif(i3 == 5):
                result = result + 'D'
                break
            elif(i3 == 9):
                result = result + 'CM'
                break
                
        for i in range(0,i2):
            if(flag2 == 1):
                result = result + 'L'
                flag2 = 0
            if(i2 == 0):
                break
            elif(i2 <= 3 ):
                result = result + 'X'
            elif(i2 == 4):
                result = result + 'XL'
                break
            elif(i2 == 5):
                result = result + 'L'
                break
            elif(i2 == 9):
                result = result + 'XC'
                break
        for i in range(0,i1):
            if(flag1 == 1):
                result = result + 'V'
                flag1 = 0
            if(i1 == 0):
                break
            elif(i1 <= 3 ):
                result = result + 'I'
            elif(i1 == 4):
                result = result + 'IV'
                break
            elif(i1 == 5):
                result = result + 'V'
                break
            elif(i1 == 9):
                result = result + 'IX'
                break
        return result
        
