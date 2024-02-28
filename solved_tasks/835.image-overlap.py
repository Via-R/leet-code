from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        A_ones = []
        B_ones = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    A_ones.append((i, j))
                if B[i][j] == 1:
                    B_ones.append((i, j))
        shifts = {}
        answer = 0
        for A_x, A_y in A_ones:
            for B_x, B_y in B_ones:
                shift = (B_x - A_x, B_y - A_y)
                shifts.setdefault(shift, 0)
                shifts[shift] += 1
                answer = max(answer, shifts[shift])

        return answer

    solver = largestOverlap
    test_cases = [([[1, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 1, 1], [0, 0, 1]]), ([[1]], [[1]]),
                  ([[0]], [[0]])]
    test_cases_answers = [(3,), (1,), (0,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
