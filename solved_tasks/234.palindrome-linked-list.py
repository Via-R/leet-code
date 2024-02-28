# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:  # TODO: adapt SolutionBase to this example and inherit from it here
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        # Sum of all positions of each digit in the number
        positions_sum = [0] * 10
        # Amounts of each digit in the number
        amounts = [0] * 10

        # Flag to mark if number is two digits and has different numbers
        different_numbers = False
        prev = head.val

        positions_sum[head.val] = 1
        amounts[head.val] = 1
        curr_idx = 1
        head = head.next

        # Sum of difference between all neighboring digits 
        num_sum = 0

        while head is not None:
            positions_sum[head.val] += curr_idx + 1
            amounts[head.val] += 1
            curr_idx += 1
            num_sum += head.val - prev
            if prev != head.val:
                different_numbers = True
            prev = head.val
            head = head.next

        # In all palindromes sum of differences between neighboring digits
        # should equal to 0
        if num_sum != 0:
            return False

        leng = curr_idx

        if leng == 1:
            return True

        if leng == 2 and different_numbers:
            return False

        base = curr_idx + 1
        middle_idx = base / 2

        # If sum of positions of each digit is a factor of base (sum of
        # 1 and length of number + 1) it means that the number is balanced
        # This in pair with zero sum of neighbors means the number is palindrome
        for idx, s in enumerate(positions_sum):
            if s / base != amounts[idx] / 2 and s != middle_idx and (s - middle_idx) % base != 0:
                return False

        return True
