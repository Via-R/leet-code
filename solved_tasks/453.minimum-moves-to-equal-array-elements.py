from typing import List

from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def minMoves(self, nums: List[int]) -> int:
        min_num = nums[0]
        num_sum = 0
        for n in nums:
            if n < min_num:
                min_num = n
            num_sum += n

        return num_sum - len(nums) * min_num

    solver = minMoves
    test_cases = [([1, 2, 3],), ([1, 1, 1],)]
    test_cases_answers = [(3,), (0,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
