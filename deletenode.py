# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        f = head
        s = f
        k = 0
        while(f != None):
            if(f.next == None):
                if(s.next == None):# only one node
                    return None
                if(n ==1):#delete the last node
                    s.next = None
                    return head
                elif(s==head and n!=1 and k!=n):#delete the first node
                    s.val = s.next.val
                    s.next = s.next.next
                else:#middle node
                    s.next = s.next.next
                break
            if(k < n):
                k = k + 1
            else:
                s = s.next
            f = f.next
        return head  
