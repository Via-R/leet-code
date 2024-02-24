from math import copysign
from functools import cache


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        start_idx = ord('a')
        row_len = 5
        moves = [['U', 'D'], ['L', 'R']]
        submit = '!'

        @cache
        def find_letter_coords(letter):
            return (ord(letter) - start_idx) // row_len, (ord(letter) - start_idx) % row_len

        @cache
        def get_move_direction(shift, axis):
            if not shift:
                return ''

            return moves[axis][(int(copysign(1, shift)) + 1) // 2] * abs(shift)

        cursor = (0, 0)
        path = ''

        for letter in target:
            new_cursor = find_letter_coords(letter)
            vertical_shift, horizontal_shift = new_cursor[0] - cursor[0], new_cursor[1] - cursor[1]
            if cursor == find_letter_coords('z'):
                path += get_move_direction(vertical_shift, 0) + get_move_direction(horizontal_shift, 1)
            else:
                path += get_move_direction(horizontal_shift, 1) + get_move_direction(vertical_shift, 0)
            path += submit
            cursor = new_cursor

        return path


def main():
    s = Solution()
    print(s.alphabetBoardPath('leet'))
    print(s.alphabetBoardPath('code'))
    print(s.alphabetBoardPath('zb'))
    print(s.alphabetBoardPath('zbz'))


if __name__ == "__main__":
    main()
