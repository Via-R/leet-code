class Solution:
    def minInsertions(self, s: str) -> int:
        middle_idx = round(len(s) / 2)
        left_dict = {}
        right_dict = {}
        odd_len_shift = len(s) % 2

        for idx in range(middle_idx):
            left_dict.setdefault(s[idx], 0)
            left_dict[s[idx]] += 1
        for idx in range(middle_idx + odd_len_shift, len(s)):
            right_dict.setdefault(s[idx], 0)
            right_dict[s[idx]] += 1

        left_letters, right_letters = set(left_dict.keys()), set(right_dict.keys())
        only_left_letters = left_letters - right_letters
        only_right_letters = right_letters - left_letters
        common_letters = left_letters.intersection(right_letters)

        result = 0
        for l in list(only_left_letters):
            result += left_dict[l]
        for l in list(only_right_letters):
            result += right_dict[l]
        for l in list(common_letters):
            result += abs(left_dict[l] - right_dict[l])

        return (result - 1) if len(s) % 2 == 0 else result


def main():
    s = Solution()
    print(s.minInsertions('zzazz'))
    print(s.minInsertions('mbadm'))
    print(s.minInsertions('leetcode'))
    print(s.minInsertions("zjveiiwvc"))


if __name__ == "__main__":
    main()
