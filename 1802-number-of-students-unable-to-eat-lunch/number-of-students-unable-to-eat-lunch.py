class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circleCnt = 0
        squareCnt = 0
        
        for i in students:
            if i == 0:
                circleCnt += 1
            else:
                squareCnt += 1
        
        for i in sandwiches:
            if i == 0 and circleCnt == 0:
                return squareCnt
            if i == 1 and squareCnt == 0:
                return circleCnt
            
            if i == 0:
                circleCnt -= 1
            else:
                squareCnt -= 1
        
        return 0