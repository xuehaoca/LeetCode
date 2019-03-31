class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        result = 0
        n1 = len(nums1)
        n2 = len(nums2)
        if( n1 < n2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
            n1 = len(nums1)
            n2 = len(nums2)
        if( n2 == 0 ):
            result =  (nums1[(n1 - 1)/2] + nums1[(n1)/2])/2.0
            return result
        a = 0
        b = n2 * 2
        while(1):
            m2 = (a + b)/2
            m1 = n1 + n2 - m2
            if(m1 != 0):
                al = nums1[(m1 - 1)/2]
            else:
                al = -sys.maxint
            if(m2 != 0):
                bl = nums2[(m2 - 1)/2]
            else:
                bl = -sys.maxint
            if(m1 != n1 * 2):
                ar = nums1[(m1)/2]
            else:
                ar = sys.maxint
            if(m2 != n2 * 2):
                br = nums2[(m2)/2]
            else:
                br = sys.maxint
            if (al > br):
                a = m2 + 1;      
            elif (bl > ar): 
                b = m2 - 1; 
            else:
                return (max(al,bl) + min(ar, br)) / 2.0
