from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if sorted(word1) == sorted(word2):
            return True

        
        w1 = [i for i in word1]
        w2 = [i for i in word2]

        a = sorted(list(set(w1)))
        b = sorted(list(set(w2)))
        if a != b : return False
        
        w1 = Counter(w1).values()
        w2 = Counter(w2).values()
        
        if sorted(w1) == sorted(w2):
            return True

        return False

        