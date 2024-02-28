from copy import copy
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        alphabet = dict()

        for l in t:
            alphabet.setdefault(l, 0)
            alphabet[l] += 1

        min_result_length = len(s) + 1
        result = ''

        idx = 0
        while idx < len(s):
            l = s[idx]

            if len(s) - idx < len(t):
                break
            if l in alphabet:
                local_result, skip_steps = self.find_local_result(s[idx:], copy(alphabet), len(t), min_result_length)
                if not local_result:
                    idx += skip_steps
                    continue
                if len(local_result) == len(t):
                    return local_result
                if len(local_result) < min_result_length:
                    min_result_length = len(local_result)
                    result = local_result
            idx += 1
        return result

    @staticmethod
    def find_local_result(substring: str, local_alphabet, local_total_numbers, max_output_length):
        '''Works with substring that starts with letter from alphabet.'''

        output = ['']
        for l in substring:

            output.append(l)
            if len(output) - 1 >= max_output_length:
                return (None, 1)

            if local_alphabet.get(l, 0) > 0:
                local_alphabet[l] -= 1
                local_total_numbers -= 1

            if local_total_numbers == 0:
                break

        return (("".join(output) or None) if not local_total_numbers else None, 1)

    solver = minWindow
    test_cases = [('ADOBECODEBANC', 'ABC'), ('a', 'a'), ('a', 'aa')]
    test_cases_answers = [('BANC',), ('a',), ('',)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
