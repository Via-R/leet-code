import itertools

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        alphabet = []
        for s in arr:
            if len(s) > len(set(s)):
                continue
            alphabet.append((len(s), set(s)))
            
        max_length = 0
            
        for combination_length in range(1, len(alphabet) + 1):
            local_max_length = 0
            for subset in itertools.combinations(alphabet, combination_length):
                length = 0
                curr_alphabet = set()
                for el in subset:
                    if len(curr_alphabet.intersection(el[1])) > 0:
                        length = 0
                        break
                    curr_alphabet.update(el[1])
                    length += el[0]
                if length > local_max_length:
                    local_max_length = length
                    
            if local_max_length > max_length:
                max_length = local_max_length
                
        return max_length