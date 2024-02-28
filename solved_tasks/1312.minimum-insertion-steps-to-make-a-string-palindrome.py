from functools import cache
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def minInsertions(self, s: str) -> int:
        @cache
        def rec(start_idx, end_idx):
            if start_idx >= end_idx:
                return 0
            if s[start_idx] == s[end_idx]:
                return rec(start_idx + 1, end_idx - 1)
            return 1 + min(rec(start_idx, end_idx - 1), rec(start_idx + 1, end_idx))

        return rec(0, len(s) - 1)

    solver = minInsertions
    test_cases = [('zzazz',), ('mbadm',), ('leetcode',), ('zjveiiwvc',), ('tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz',)]
    test_cases_answers = [(0,), (2,), (5,), (5,), (25,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
