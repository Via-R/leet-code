from copy import copy
from time import time

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        
        alphabet = dict()
        
        for l in t:
            alphabet.setdefault(l, 0)
            alphabet[l] += 1
        
        min_window_size = len(s) + 1
        result = ''
        
        left, right = 0, 0
        new_numbers = len(t)
        while right < len(s):
            print(f"{s[left:right+1]=}, {left=}, {right=}")
            right_shift = self.findNewRightShift(s[right:], alphabet, new_numbers)
            print(f"{right_shift=}")
            if right_shift is None:
                break
            right += right_shift
            left_shift = self.findNewLeftShift(s[left:right+1], alphabet)
            print(f"{left_shift=}")
            if left_shift is None:
                break
            left += left_shift
            local_result = s[left:right+1]
            if len(local_result) < min_window_size:
                min_window_size = len(local_result)
                result = local_result
            print(f"{local_result=}")
            alphabet[s[left]] += 1
            new_numbers = 1
            left += 1
            right += 1
            
            
        return result
        
    @staticmethod            
    def findNewRightShift(substring, alphabet, new_numbers):
        print(f"Right {alphabet=}, {new_numbers=}")
        for idx, l in enumerate(substring):
            if l in alphabet:
                alphabet[l] -= 1
                if alphabet[l] >= 0:
                    new_numbers -= 1
            if new_numbers == 0:
                return idx

        return None
    
    @staticmethod
    def findNewLeftShift(substring, alphabet):
        for idx, l in enumerate(substring):
            if l not in alphabet:
                continue
            if alphabet[l] + 1 > 0:
                return idx
            alphabet[l] += 1
        return None
                
if __name__ == "__main__":
    s = "aaaaaaaaaaaabbbbbcdd"
    t = "abcdd"
    # "abbbbbcdd"
    ss = Solution()
    st = time()
    answer = ss.minWindow(s, t)
    et = time()
    print(answer)
    print(f"Estimated time: {et-st} seconds")