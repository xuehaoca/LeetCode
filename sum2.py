# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        l5 = ListNode(0)
        l6 = ListNode(0)
        l5.next = l3
        while(l1 != None and l2 != None):
            l4 = ListNode(0)
            a = l1.val + l2.val + l3.val
            if(a >= 10):
                b = a - 10
                l3.val = b
                l4.val = l4.val + 1
                l3.next = l4
                l6.next = l3
                l3 = l4
            else: 
                l3.val = a
                l3.next = l4
                l6.next = l3
                l3 = l4
            l1 = l1.next
            l2 = l2.next
        if(l1 == None and l2 != None):
            while(l2 != None):
                l4 = ListNode(0)
                l3.val = l2.val + l3.val
                if(l3.val >= 10):
                    b = l3.val - 10
                    l3.val = b
                    l4.val = l4.val + 1
                    l3.next = l4
                    l6.next = l3
                    l3 = l4
                    l2 = l2.next
                else: 
                    l3.next = l4
                    l6.next = l3
                    l3 = l4
                    l2 = l2.next
        elif(l2 == None and l1 != None):
            while(l1 != None):
                l4 = ListNode(0)
                l3.val = l1.val + l3.val
                if(l3.val >= 10):
                    b = l3.val - 10
                    l3.val = b
                    l4.val = l4.val + 1
                    l3.next = l4
                    l6.next = l3
                    l3 = l4
                    l1 = l1.next
                else: 
                    l3.next = l4
                    l6.next = l3
                    l3 = l4
                    l1 = l1.next
        if(l6.next.next.val == 0): l6.next.next = None
        return l5.next   
        
        
