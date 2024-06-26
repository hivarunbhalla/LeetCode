class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        
        a = 0
        b = 1
        c = 1
        
        for i in range(3, n+1):
            a, b, c = b, c, a+b+c
        return c