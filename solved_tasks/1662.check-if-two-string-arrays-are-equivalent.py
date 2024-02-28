from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

    solver = arrayStringsAreEqual
    test_cases = [(["ab", "c"], ["a", "bc"]), (["a", "cb"], ["ab", "c"]), (["abc", "d", "defg"], ["abcddefg"])]
    test_cases_answers = [(True,), (False,), (True,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
