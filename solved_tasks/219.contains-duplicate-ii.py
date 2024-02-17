class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == 1:
            return False
        
        history = dict()
        
        for idx, num in enumerate(nums):
            if num in history and idx - history[num] <= k:
                return True
            history[num] = idx
        
        return False