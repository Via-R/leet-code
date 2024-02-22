class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def memoized_rec(old_rec):
            memo = {}

            def memo_rec(*args):
                if args in memo:
                    return memo[args]

                new_value = old_rec(*args)
                memo[args] = new_value

                return new_value

            return memo_rec

        @memoized_rec
        def rec(idx1, idx2):
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0
            if text1[idx1] == text2[idx2]:
                return 1 + rec(idx1 + 1, idx2 + 1)

            return max(rec(idx1 + 1, idx2), rec(idx1, idx2 + 1))

        return rec(0, 0)

def main():
    s = Solution()
    print(s.longestCommonSubsequence('abcde', 'ace'))
    print(s.longestCommonSubsequence('abc', 'abc'))
    print(s.longestCommonSubsequence('abc', 'def'))


if __name__ == "__main__":
    main()
