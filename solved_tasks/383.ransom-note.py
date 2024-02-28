from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = dict()
        for l in magazine:
            alphabet.setdefault(l, 0)
            alphabet[l] += 1

        for l in ransomNote:
            if alphabet.get(l, 0) == 0:
                return False

            alphabet[l] -= 1

        return True

    solver = canConstruct
    test_cases = [('a', 'b'), ('aa', 'ab'), ('aa', 'aab')]
    test_cases_answers = [(False,), (False,), (True,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
