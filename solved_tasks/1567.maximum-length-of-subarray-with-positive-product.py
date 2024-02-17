from typing import List


class Solution:
    def get_possible_sub_array_limit(self, nums, from_idx):
        # search for the first non-zero element
        start_idx = from_idx
        for idx, num in enumerate(nums[from_idx:]):
            if num != 0:
                start_idx = idx + from_idx
                break
        else:
            raise Exception('No possible answer here')
        # search for the next zero element (or the end of the array)
        end_idx = None
        for idx, num in enumerate(nums[start_idx:]):
            if num == 0:
                end_idx = idx + start_idx
                break

        end_idx = end_idx or len(nums)

        return start_idx, end_idx

    def getMaxLen(self, nums: List[int]) -> int:
        if not len(nums) or len(nums) == 1 and nums[0] <= 0:
            return 0
        if len(nums) == 1 and nums[0] > 0:
            return 1

        valid_sub_arrays_limits = []

        if 0 in nums:
            try:
                sub_array_start_idx, sub_array_end_idx = self.get_possible_sub_array_limit(nums, 0)
            except:
                return 0

            valid_sub_arrays_limits.append((sub_array_start_idx, sub_array_end_idx))

            while sub_array_end_idx != len(nums):
                try:
                    sub_array_start_idx, sub_array_end_idx = self.get_possible_sub_array_limit(nums,
                                                                                               sub_array_end_idx + 1)
                    valid_sub_arrays_limits.append((sub_array_start_idx, sub_array_end_idx))
                except:
                    break

        else:
            valid_sub_arrays_limits = [(0, len(nums))]

        sub_array_lens = [0] * len(valid_sub_arrays_limits)
        for idx, (sub_array_start_idx, sub_array_end_idx) in enumerate(valid_sub_arrays_limits):
            sub_nums = nums[sub_array_start_idx: sub_array_end_idx]
            if sum([1 for num in sub_nums if num < 0]) % 2 == 0:
                sub_array_lens[idx] = len(sub_nums)
                continue

            left_idx = next(i for i, v in enumerate(sub_nums) if v < 0)
            mirrored_right_idx = next(i for i, v in enumerate(sub_nums[::-1]) if v < 0)
            right_idx = len(sub_nums) - mirrored_right_idx - 1
            if left_idx == right_idx:
                sub_array_lens[idx] = max(self.getMaxLen(sub_nums[0:left_idx]), self.getMaxLen(sub_nums[left_idx + 1:]))
                continue

            if left_idx > mirrored_right_idx:
                sub_array_lens[idx] = right_idx
                continue

            sub_array_lens[idx] = len(sub_nums) - left_idx - 1

        return max(sub_array_lens)


def main():
    s = Solution()
    print(s.getMaxLen([1, -2, -3, 4]))
    print(s.getMaxLen([0, 1, -2, -3, -4]))
    print(s.getMaxLen([-1, -2, -3, 0, 1]))
    print(s.getMaxLen([0, 0, 0, 0, 0, 1, -1, 1, 0, 0, 0, 0, 1, 0, 0, -1, 1, -1, 1]))


if __name__ == "__main__":
    main()
