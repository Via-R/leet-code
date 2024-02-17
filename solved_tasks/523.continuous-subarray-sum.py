class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for start_idx in range(len(nums) - 1):
            for end_idx in range(start_idx + 1, len(nums)):
                if sum(nums[start_idx:end_idx+1]) % k == 0:
                    return True
                
        return False