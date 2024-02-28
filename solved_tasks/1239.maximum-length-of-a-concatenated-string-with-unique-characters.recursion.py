from typing import List

from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)

        def dfs(start_idx, local_result):
            if len(set(local_result)) < len(local_result):
                return 0

            best_result = len(local_result)
            for idx in range(start_idx, n):
                dfs_result = dfs(idx + 1, local_result + arr[idx])
                best_result = max(best_result, dfs_result)

            return best_result

        return dfs(0, '')

    solver = maxLength
    test_cases = [(["un", "iq", "ue"],), (["cha", "r", "act", "ers"],), (["abcdefghijklmnopqrstuvwxyz"],)]
    test_cases_answers = [(4,), (6,), (26,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
