from copy import copy
from typing import Dict, List
from solutions_base.core import SolutionBase, SolutionTesting


class Solution(SolutionBase):
    @staticmethod
    def findDistance(gene_a: str, gene_b: str) -> int:
        result = 0
        for genome_a, genome_b in zip(gene_a, gene_b):
            if genome_a != genome_b:
                result += 1

        return result

    @staticmethod
    def bfs(genes_with_banks: Dict[str, List[str]], target_gene: str, depth: int) -> int:
        if not len(genes_with_banks):
            return -1

        new_genes_with_banks = {}
        for gene, bank in genes_with_banks.items():
            if gene == target_gene:
                return depth
            for new_gene in bank:
                if Solution.findDistance(gene, new_gene) == 1:
                    new_bank = copy(bank)
                    new_bank.remove(new_gene)
                    new_genes_with_banks[new_gene] = new_bank

        return Solution.bfs(copy(new_genes_with_banks), target_gene, depth + 1)

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        return self.bfs({startGene: copy(bank)}, endGene, 0)

    solver = minMutation
    test_cases = [('AACCGGTT', 'AACCGGTA', ["AACCGGTA"]), ('AACCGGTT', 'AAACGGTA',
                                                           ["AACCGGTA", "AACCGCTA", "AAACGGTA"])]
    test_cases_answers = [(1,), (2,)]


def main():
    s = Solution()
    test_suite = SolutionTesting(s)
    test_suite.test_answers()


if __name__ == "__main__":
    main()
