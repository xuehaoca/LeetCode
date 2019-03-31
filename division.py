class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        result = 0
        if(divisor == 0):
            return 0
        flag = 1
        if(abs(divisor) == 1):
            result = dividend * divisor
            if(result < -pow(2,31) or result > (pow(2,31)-1)):
                result = pow(2,31)-1
            return result
        if(dividend == 0):
            return 0
        if(dividend < 0):
            flag = flag * (-1)
            dividend = dividend * (-1)
        if(divisor < 0):
            flag = flag * (-1)
            divisor = divisor * (-1)
        factor = divisor
        d = dividend
        while(factor <= d):
            t = divisor
            p = 1
            while( t+t < d ):
                t = t + t
                p = p + p
            result = result + p
            d = d - t
        result = result * flag
        if(result < -pow(2,31) or result > (pow(2,31)-1)):
            result = pow(2,31)-1
            return result
        return result
