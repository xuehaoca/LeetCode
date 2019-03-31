import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mind = sys.maxint
        lens = len(nums)
        sumr = 0
        f2 = 0
        i = 0
        j = 1
        k = 2
        if(lens < 3):
            for i in range(0,lens):
                sumr = sumr + nums[i]
            return sumr
        else:
            nums.sort()
            mid = 0
            low = 0
            high = 0
            sumr = nums[0] + nums[1] + nums[2]
            while(i<lens):
                while(j<lens):
                    mid = j + 1
                    if(mid == lens):
                        break
                    low = mid
                    high = lens - 1
                    while(k<lens):
                      #  print i,j,k,mid,sumr,low,high
                        k = mid
                        N = nums[i] + nums[j] + nums[k]
                        if( abs(N-target) == 0):
                            return N 
                        elif(abs(N-target) <= abs(sumr-target)): 
                            sumr = N
                        if(N > target):
                            high = mid
                            mid = (mid + low )/2                 
                        else:
                            low = mid
                            mid = (mid + high)/2
                        if((high-low)<=1):
                            if(N > target):
                                if(k == j+1):
                                    break
                                N = nums[i] + nums[j] + nums[k-1]
                                N2 = nums[i] + nums[j] + nums[k]
                                #print i,j,k
                                #print N,N2
                                if(abs(N-target) <= abs(N2-target)):
                                    if(abs(sumr-target) > abs(N-target)):sumr = N
                                    break
                                else:
                                    if(abs(sumr-target) > abs(N2-target)):sumr = N2
                                    break
                            else:
                                if(k == lens-1):
                                    break
                                N = nums[i] + nums[j] + nums[k+1]
                                N2 = nums[i] + nums[j] + nums[k]
                               # print i,j,k
                                #print N,N2
                                if(abs(N-target) <= abs(N2-target)):
                                    if(abs(sumr-target) > abs(N-target)):sumr = N
                                    break
                                else:
                                    if(abs(sumr-target) > abs(N2-target)):sumr = N2
                                    break
                    j = j + 1
                i = i + 1
                j = i + 1
                k = j + 1
            return sumr
                            
