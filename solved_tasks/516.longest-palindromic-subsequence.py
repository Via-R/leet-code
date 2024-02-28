from functools import cache
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def rec(left_idx, right_idx):
            if left_idx > right_idx:
                return 0
            if left_idx == right_idx:
                return 1
            if s[left_idx] == s[right_idx]:
                return 2 + rec(left_idx + 1, right_idx - 1)

            return max(rec(left_idx, right_idx - 1), rec(left_idx + 1, right_idx))

        return rec(0, len(s) - 1)

    solver = longestPalindromeSubseq
    test_cases = [('bbbab',), ('cbbd',)]
    test_cases_answers = [(4,), (2,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
