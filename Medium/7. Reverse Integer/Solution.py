class Solution:
    def reverse(self, x: int) -> int:
        s = '-' if x<0 else ''
        r = int(s+str(abs(x))[::-1])
        if r<-2**31 or r>2**31-1:
            return 0
        return r