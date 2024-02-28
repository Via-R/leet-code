from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    letter_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        skip_next_letter = False
        for idx in range(len(s)):
            if skip_next_letter:
                skip_next_letter = False
                continue

            if idx + 1 < len(s) and self.letter_values[s[idx]] < self.letter_values[s[idx + 1]]:
                result += self.letter_values[s[idx + 1]] - self.letter_values[s[idx]]
                skip_next_letter = True
                continue

            result += self.letter_values[s[idx]]

        return result

    solver = romanToInt
    test_cases = [('III',), ('LVIII',), ('MCMXCIV',)]
    test_cases_answers = [(3,), (58,), (1994,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
