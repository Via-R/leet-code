from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        if not len(nums) or len(nums) == 1 and nums[0] <= 0:
            return 0
        if len(nums) == 1 and nums[0] > 0:
            return 1

        if 0 in nums:
            divider_idx = nums.index(0)
            return max(self.getMaxLen(nums[0:divider_idx]), self.getMaxLen(nums[divider_idx+1:]))

        if sum([1 for num in nums if num < 0]) % 2 == 0:
            return len(nums)

        left_idx = next(i for i,v in enumerate(nums) if v < 0)
        mirrored_right_idx = next(i for i, v in enumerate(nums[::-1]) if v < 0)
        right_idx = len(nums) - mirrored_right_idx - 1
        if left_idx == right_idx:
            return max(self.getMaxLen(nums[0:left_idx]), self.getMaxLen(nums[left_idx+1:]))

        if left_idx > mirrored_right_idx:
            return right_idx

        return len(nums) - left_idx - 1

def main():
    s = Solution()
    print(s.getMaxLen([1,-2,-3,4]))
    print(s.getMaxLen([0, 1, -2, -3, -4]))
    print(s.getMaxLen([-1, -2, -3, 0, 1]))


if __name__ == "__main__":
    main()
