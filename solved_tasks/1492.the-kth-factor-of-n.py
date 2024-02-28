from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        try:
            return next(x for x in range(1, n + 1) if n % x == 0 and ((count := count + 1) == k))
        except StopIteration:
            return -1

    solver = kthFactor
    test_cases = [(12, 3), (7, 2), (4, 4)]
    test_cases_answers = [(3,), (7,), (-1,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
