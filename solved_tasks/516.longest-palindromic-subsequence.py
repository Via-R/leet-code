from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def rec(left_idx, right_idx):
            if left_idx > right_idx:
                return 0
            if left_idx == right_idx:
                return 1
            if s[left_idx] == s[right_idx]:
                return 2 + rec(left_idx + 1, right_idx - 1)

            return max(rec(left_idx, right_idx - 1), rec(left_idx + 1, right_idx))

        return rec(0, len(s) - 1)


def main():
    s = Solution()
    print(s.longestPalindromeSubseq('bbbab'))
    print(s.longestPalindromeSubseq('cbbd'))


if __name__ == "__main__":
    main()
