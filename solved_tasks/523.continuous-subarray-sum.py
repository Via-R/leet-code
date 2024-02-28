from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for start_idx in range(len(nums) - 1):
            for end_idx in range(start_idx + 1, len(nums)):
                if sum(nums[start_idx:end_idx + 1]) % k == 0:
                    return True

        return False

    solver = checkSubarraySum
    test_cases = [([23, 2, 4, 6, 7], 6), ([23, 2, 6, 4, 7], 6), ([23, 2, 6, 4, 7], 13)]
    test_cases_answers = [(True,), (True,), (False,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
