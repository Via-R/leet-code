import heapq
from typing import List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    def hIndex(self, citations: List[int]) -> int:
        inv_citations = [-c for c in citations if c != 0]
        positive_citations_len = len(inv_citations)
        heapq.heapify(inv_citations)
        count = 1
        try:
            while -heapq.heappop(inv_citations) >= count:
                count += 1

        except IndexError:
            return positive_citations_len

        return count - 1

    solver = hIndex
    test_cases = [([3, 0, 6, 1, 5],), ([1, 3, 1],), ([1, 7, 9, 4],), ([4, 4, 0, 0],)]
    test_cases_answers = [(3,), (1,), (3,), (2,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
