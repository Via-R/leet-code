class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numbers = set()
        s = (len(nums) * (len(nums) + 1)) // 2
        a = None
        for n in nums:
            if n in numbers:
                a = n
            else:
                numbers.add(n)
                s -= n
                
        return a, s