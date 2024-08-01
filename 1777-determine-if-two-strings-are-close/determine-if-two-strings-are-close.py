class Solution:
    def closeStrings(self,a:str,b:str)->bool:
        x,y=[],[] 
        for i in set(a):
            x.append(a.count(i)) 
            y.append(b.count(i))
        return sorted(x)==sorted(y)