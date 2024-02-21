from typing import List
from math import sqrt


class Solution:
    def find_right_divisor(self, left_divisor, num):
        right_divisor = left_divisor + 1
        while left_divisor * right_divisor <= num + 2:
            if left_divisor * right_divisor == num + 1 or left_divisor * right_divisor == num + 2:
                return right_divisor
            right_divisor += 1

        return None

    def closestDivisors(self, num: int) -> List[int]:
        middle = int(sqrt(num)) + 1
        if middle ** 2 == num + 1 or middle ** 2 == num + 2:
            return [middle, middle]

        left_divisor = middle
        while left_divisor >= 1:
            right_divisor = self.find_right_divisor(left_divisor, num)
            if right_divisor:
                return [left_divisor, right_divisor]
            left_divisor -= 1

        return [-1, -1]


def main():
    s = Solution()
    print(s.closestDivisors(8))
    print(s.closestDivisors(123))
    print(s.closestDivisors(999))
    print(s.closestDivisors(1))
    print(s.closestDivisors(688427155))


if __name__ == "__main__":
    main()
