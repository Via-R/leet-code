from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
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

        return [a, s]

    solver = findErrorNums
    test_cases = [([1, 2, 2, 4],), ([1, 1],)]
    test_cases_answers = [([2, 3],), ([1, 2],)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
