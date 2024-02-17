from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        array_missed_amount = arr[-1] - len(arr)
        if k > array_missed_amount:
            return arr[-1] + k - array_missed_amount

        missed_amount = 0
        prev = 0
        for num in arr:
            missed_amount += num - prev - 1
            if missed_amount >= k:
                return num - (missed_amount - k + 1)
            prev = num

def main():
    s = Solution()
    print(s.findKthPositive([2, 3, 4, 7, 11], 5))
    print(s.findKthPositive([2, 7, 11], 5))
    print(s.findKthPositive([1, 2, 3, 4], 2))
    print(s.findKthPositive([2], 1))
    print(s.findKthPositive([3, 10], 2))


if __name__ == "__main__":
    main()
