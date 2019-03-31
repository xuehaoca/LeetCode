class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        lens = len(height)
        right = lens-1
        maxs = 0
        while(left != right):
            maxs = max(maxs,min(height[left],height[right])*(right-left))
            if(height[left]<height[right]):
                left = left + 1
            else:
                right = right - 1
        return maxs
