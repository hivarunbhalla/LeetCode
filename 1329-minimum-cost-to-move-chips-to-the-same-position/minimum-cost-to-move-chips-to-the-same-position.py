class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ODD = EVEN = 0
        n = len(position)
        for i in position:
            if i%2 == 0:
                EVEN += 1
            else:
                ODD += 1

        return min(EVEN, ODD)