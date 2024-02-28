from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def fizzBuzz(self, n: int) -> List[str]:
        return [w if w != '' else str(i) for i in range(1, n + 1) if (w := 'Fizz'[i % 3 * 4:(i % 3 + 1) * 4] + 'Buzz'[i % 5 * 4:(i % 5 + 1) * 4], 1)]

    solver = fizzBuzz
    test_cases = [(3,), (5,), (15,)]
    test_cases_answers = [(["1", "2", "Fizz"],), (["1", "2", "Fizz", "4", "Buzz"],), (
        ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"],)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
