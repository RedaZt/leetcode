class Solution:
    def romanToInt(self, s: str) -> int:
        p=0
        r=0
        d=dict(I=1,IV=4,V=5,X=10,L=50,C=100,D=500,M=1000)
        for x in s: 
            v=d[x]
            r-=2*p*(v>p)
            p=v
            r+=v
        return r