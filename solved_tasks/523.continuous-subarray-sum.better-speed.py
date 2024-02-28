from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainders = {0: -1}
        curr_rem = 0
        for i, num in enumerate(nums):
            curr_rem = (curr_rem + num) % k
            if curr_rem in remainders:
                if remainders[curr_rem] < i-1:
                    return True
            else:
                remainders[curr_rem] = i
                
        return False

    solver = checkSubarraySum
    test_cases = [([23,2,4,6,7], 6), ([23,2,6,4,7], 6), ([23,2,6,4,7], 13)]
    test_cases_answers = [(True,), (True,), (False,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()