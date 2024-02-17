# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        if head.next is None:
            return True
        
        fast, slow = head.next, head
        n = 0
        while fast is not None and fast.next is not None:
            slow, fast = slow.next, fast.next.next
            n+=1
        
        pointer = slow
        prev = None
        while pointer is not None:
            pointer.next, prev, pointer = prev, pointer, pointer.next
        
        left = head
        right = prev
        for _ in range(n+1):
            if left.val != right.val:
                return False
            left, right = left.next, right.next
            
        return True
            
        