from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        l = [1]
        r=[l]
        for i in range(numRows-1):
            l = l[:1]+[i+j for i,j in zip(l,l[1:])]+l[-1:]
            r += l,
        return r