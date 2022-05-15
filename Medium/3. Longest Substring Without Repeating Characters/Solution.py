# Slow af

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        r=0
        n=len(s)
        for i in range(n):
            if len(s)-i > r :
                for j in range(i+1,n+1):
                    t = s[i:j]
                    if j-i > r:
                        if any(t.count(x)>1 for x in t):
                            break
                        elif len(t) > r:
                            r = len(t)
        return r