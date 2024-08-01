class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wc1 = Counter(word1)
        wc2 = Counter(word2)
        if (len(word1)!= len(word2) 
            or set(wc1.keys()) != set(wc2.keys())
            or sorted(wc1.values())) != sorted(wc2.values()):
            return False 

        return True