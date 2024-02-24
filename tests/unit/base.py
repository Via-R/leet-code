import unittest

from solutions_base.core import SolutionBase, BaseError


class TestBaseExceptions(unittest.TestCase):
    def test_solver_presence(self):
        class Solution(SolutionBase):
            test_cases = []
            test_cases_answers = []

        with self.assertRaises(BaseError) as context:
            Solution()

        self.assertIn('"solver"', str(context.exception))

    def test_test_cases_presence(self):
        class Solution(SolutionBase):
            def solver(self):
                return self

            test_cases_answers = []

        with self.assertRaises(BaseError) as context:
            Solution()

        self.assertIn('"test_cases"', str(context.exception))

    def test_test_cases_answers_presence(self):
        class Solution(SolutionBase):
            def solver(self):
                return self

            test_cases = []

        with self.assertRaises(BaseError) as context:
            Solution()

        self.assertIn("test_cases_answers", str(context.exception))

    def test_test_cases_type(self):
        class Solution(SolutionBase):
            def solver(self):
                return self

            test_cases = [[1]]
            test_cases_answers = []

        with self.assertRaises(BaseError) as context:
            Solution()

        self.assertRegex(str(context.exception), r'"test_cases".+must be of type')

    def test_test_cases_answers_type(self):
        class Solution(SolutionBase):
            def solver(self):
                return self

            test_cases = [(1,)]
            test_cases_answers = [[1]]

        with self.assertRaises(BaseError) as context:
            Solution()

        self.assertRegex(str(context.exception), r'"test_cases_answers".+must be of type')

    def test_test_cases_zero_length(self):
        class Solution(SolutionBase):
            def solver(self):
                return self

            test_cases = []
            test_cases_answers = []

        with self.assertRaises(BaseError) as context:
            Solution()

        self.assertRegex(str(context.exception), r'must match the length.+and be greater than 0')

    def test_test_cases_length_mismatch(self):
        class Solution(SolutionBase):
            def solver(self):
                return self

            test_cases = [(1,)]
            test_cases_answers = [(1,), (2,)]

        with self.assertRaises(BaseError) as context:
            Solution()

        self.assertRegex(str(context.exception), r'must match the length')

    def test_test_valid_solution(self):
        class Solution(SolutionBase):
            def solver(self):
                return self

            test_cases = [(1,)]
            test_cases_answers = [(1,)]

        Solution()

