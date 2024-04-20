def vow(s):
    v = ['a', 'e', 'i', 'o', 'u']
    s= s.lower()
    cnt = 0
    for i in s:
        if i in v:
            cnt += 1

    return cnt

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        i , j = 0, 0
        c = 0
        m = 0

        while j < len(s):

            if vow(s[j]) : 
                c += 1


            if (j-i+1) == k:
                m = max(c, m)
                if vow(s[i]): c -= 1

                i += 1
            
            j += 1
        return m
            
