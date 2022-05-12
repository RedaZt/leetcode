class Solution(object):
    def isNumber(self, s):
        try :
            if not any(x.isnumeric()for x in s): 
                return False
            a = float(s)
            return True
        except:
            return False