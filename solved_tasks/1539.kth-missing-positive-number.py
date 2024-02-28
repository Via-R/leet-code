from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def findKthPositive(self, arr: List[int], k: int) -> int:
        array_missed_amount = arr[-1] - len(arr)
        if k > array_missed_amount:
            return arr[-1] + k - array_missed_amount

        missed_amount = 0
        prev = 0
        for num in arr:
            missed_amount += num - prev - 1
            if missed_amount >= k:
                return num - (missed_amount - k + 1)
            prev = num

    solver = findKthPositive
    test_cases = [([2, 3, 4, 7, 11], 5), ([2, 7, 11], 5), ([1, 2, 3, 4], 2), ([2], 1), ([3, 10], 2)]
    test_cases_answers = [(9,), (6,), (6,), (1,), (2,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
