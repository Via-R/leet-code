class Solution:
    letter_values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def romanToInt(self, s: str) -> int:
        result = 0
        skip_next_letter = False
        for idx in range(len(s)):
            if skip_next_letter:
                skip_next_letter = False
                continue

            if idx + 1 < len(s) and self.letter_values[s[idx]] < self.letter_values[s[idx + 1]]:
                result += self.letter_values[s[idx + 1]] - self.letter_values[s[idx]]
                skip_next_letter = True
                continue

            result += self.letter_values[s[idx]]

        return result
