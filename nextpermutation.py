class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        temp = nums[lens-1]
        t = lens - 2
        while(nums[t] >= temp):
            temp = nums[t]
            t = t -1 
            if(t<0):
                break
        k=0
        if(t == -1):
            nums.sort()
        elif t!= -2:
            for i in range(t+1,lens):
                if(nums[i] > nums[t]):
                    continue
                else:
                    k = i
                    break
            k = k-1
            temp = nums[t]
            nums[t] = nums[k]
            nums[k] = temp
            print t,nums[t+1:lens]
            new = list()
            for i in range(t+1,lens):
                new.append(nums[i])
            new.sort()
            for i in range(t+1,lens):
                nums[i] = new[i-t-1]
