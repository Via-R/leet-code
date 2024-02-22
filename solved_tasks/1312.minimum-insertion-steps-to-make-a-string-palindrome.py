class Solution:
    def minInsertions(self, s: str) -> int:
        def make_memo_rec(rec):
            memo = {}

            def memo_rec(*args):
                if args in memo:
                    return memo[args]
                new_result = rec(*args)
                memo[args] = new_result
                return new_result

            return memo_rec

        @make_memo_rec
        def rec(start_idx, end_idx):
            if start_idx >= end_idx:
                return 0
            if s[start_idx] == s[end_idx]:
                return rec(start_idx + 1, end_idx - 1)
            return 1 + min(rec(start_idx, end_idx - 1), rec(start_idx + 1, end_idx))

        return rec(0, len(s) - 1)


def main():
    s = Solution()
    print(s.minInsertions('zzazz'))
    print(s.minInsertions('mbadm'))
    print(s.minInsertions('leetcode'))
    print(s.minInsertions("zjveiiwvc"))
    print(s.minInsertions("tldjbqjdogipebqsohdypcxjqkrqltpgviqtqz"))


if __name__ == "__main__":
    main()
