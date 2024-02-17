from typing import List


class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        positive_product_length, negative_product_length = 0, 0
        if nums[0] > 0:
            positive_product_length = 1
        elif nums[0] < 0:
            negative_product_length = 1

        answer = positive_product_length

        for num_idx in range(1, len(nums)):
            if nums[num_idx] > 0:
                positive_product_length = positive_product_length + 1
                negative_product_length = negative_product_length + 1 if negative_product_length > 0 else 0
            elif nums[num_idx] < 0:
                positive_product_length, negative_product_length = negative_product_length + 1 if negative_product_length > 0 else 0, positive_product_length + 1
            else:
                positive_product_length, negative_product_length = 0, 0

            answer = max(answer, positive_product_length)

        return answer


def main():
    s = Solution()
    print(s.getMaxLen([1, -2, -3, 4]))
    print(s.getMaxLen([0, 1, -2, -3, -4]))
    print(s.getMaxLen([-1, -2, -3, 0, 1]))


if __name__ == "__main__":
    main()
