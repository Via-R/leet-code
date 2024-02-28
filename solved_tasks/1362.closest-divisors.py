from typing import List
from math import sqrt
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def find_biggest_divisor(self, num, max_divisor=1):
        divisor = int(sqrt(num)) + 1
        if divisor ** 2 == num:
            return [divisor, divisor]

        while divisor >= (max_divisor or 1):
            if num % divisor == 0:
                return divisor
            divisor -= 1

        return None

    def closestDivisors(self, num: int) -> List[int]:
        first_divisor = self.find_biggest_divisor(num + 1)
        second_divisor = self.find_biggest_divisor(num + 2, first_divisor)
        bigger_divisor = max(first_divisor or -1, second_divisor or -1)
        if bigger_divisor == -1:
            return [-1, -1]
        if first_divisor == bigger_divisor:
            return [first_divisor, (num + 1) // first_divisor]
        if second_divisor == bigger_divisor:
            return [second_divisor, (num + 2) // second_divisor]

        return [-1, -1]

    solver = closestDivisors
    test_cases = [(8,), (123,), (999,), (1,), (688427155,)]
    test_cases_answers = [([3, 3],), ([5, 25],), ([25, 40],), ([2, 1],), ([2409, 285773],)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
