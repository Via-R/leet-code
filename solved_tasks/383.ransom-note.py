class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabet = dict()
        for l in magazine:
            alphabet.setdefault(l, 0)
            alphabet[l] += 1
            
        for l in ransomNote:
            if alphabet.get(l, 0) == 0:
                return False
            
            alphabet[l] -= 1
            
        return True
            