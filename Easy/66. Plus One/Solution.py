class Solution(object):
    def plusOne(self, digits):
        return list(str(int(''.join(map(str,digits)))+1))
