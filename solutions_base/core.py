import unittest


class BaseError(Exception):
    """Custom exception for invalid class configuration."""

    pass


class SolutionBase:
    """Virtual class for all Solution classes.

    Each LeetCode "Solution" class must be a subclass of SolutionBase.
    It provides the subclass with a testing method and initial checks
    for proper configuration."""

    solver = None
    test_cases = None
    test_cases_answers = None

    def __init__(self):
        if getattr(self, 'solver') is None:
            raise BaseError("You must add a \"solver\" method that contains the solution's entry point")
        if getattr(self, 'test_cases') is None:
            raise BaseError("You must add a \"test_cases\" field that contains all known test cases")
        if getattr(self, 'test_cases_answers') is None:
            raise BaseError("You must add a \"test_cases_answers\" field that contains all known test cases answers")
        if not type(self.test_cases) is list or not all(type(tc) is tuple for tc in self.test_cases):
            raise BaseError('"test_cases" must be of type List[Tuple[...]]')
        if not type(self.test_cases_answers) is list or not all(type(tca) is tuple for tca in self.test_cases_answers):
            raise BaseError('"test_cases_answers" must be of type List[Tuple[...]]')
        if not (len(self.test_cases) == len(self.test_cases_answers) > 0):
            raise BaseError(
                ('The length of "test_cases" must match the length of "test_cases_answers" and be greater than 0.\n'
                 f'Assertion {len(self.test_cases)} == {len(self.test_cases_answers)} > 0 failed.')
            )


class SolutionTesting(unittest.TestCase):
    """Base class for unit testing of test cases.

    A class instance of SolutionBase subclass must be provided in constructor."""

    def __init__(self, s: SolutionBase):
        super().__init__()
        self.s = s

    def test_answers(self):
        n = len(self.s.test_cases)
        for idx, (test_case_args, test_case_answer) in enumerate(zip(self.s.test_cases, self.s.test_cases_answers)):
            answer = self.s.solver(*test_case_args)
            answer = (answer,) if not type(answer) is tuple else answer

            print(f'Test case {idx + 1}/{n}...', end=' ')
            try:
                self.assertEqual(answer, test_case_answer)
            except AssertionError:
                print('Failure')
                raise

            print(f'Success')
