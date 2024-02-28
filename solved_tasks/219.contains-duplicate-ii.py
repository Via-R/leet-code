from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) == 1:
            return False

        history = dict()

        for idx, num in enumerate(nums):
            if num in history and idx - history[num] <= k:
                return True
            history[num] = idx

        return False

    solver = containsNearbyDuplicate
    test_cases = [([1, 2, 3, 1], 3), ([1, 0, 1, 1], 1), ([1, 2, 3, 1, 2, 3], 2)]
    test_cases_answers = [(True,), (True,), (False,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
