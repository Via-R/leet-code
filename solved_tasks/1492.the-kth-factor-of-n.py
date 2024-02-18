from typing import List


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        try:
            return next(x for x in range(1, n+1) if n % x == 0 and ((count := count + 1) == k))
        except StopIteration:
            return -1


def main():
    s = Solution()
    print(s.kthFactor(12, 3))
    print(s.kthFactor(7, 2))
    print(s.kthFactor(4, 4))


if __name__ == "__main__":
    main()
