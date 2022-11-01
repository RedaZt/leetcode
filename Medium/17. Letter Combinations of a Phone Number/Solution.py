class Solution(object):
    def letterCombinations(self, digits):
        d = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
        }
        if digits == '':
            return []
        else:
            def F(c):
                if len(c) == 1:
                    return list(d[c])
                else:
                    f = []
                    for x in d[c[0]]:
                        for y in F(c[1:]):
                            f += [x + y]
                    return f
            return F(digits)

class Solution(object):
    def letterCombinations(self, digits):
        d = {
        '2' : ['a', 'b', 'c'],
        '3' : ['d', 'e', 'f'],
        '4' : ['g', 'h', 'i'],
        '5' : ['j', 'k', 'l'],
        '6' : ['m', 'n', 'o'],
        '7' : ['p', 'q', 'r', 's'],
        '8' : ['t', 'u', 'v'],
        '9' : ['w', 'x', 'y', 'z'],
        }
        if digits=='':
            return []
        else:
            def F(c):
                if len(c) == 1:
                    return d[c]
                else:
                    f=[]
                    for x in d[c[0]]:
                        for y in F(c[1:]):
                            f+=[x+y]
                    return f
            return F(digits)
        
class Solution(object):
    def letterCombinations(self, digits):
        d = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
        }
        if digits == '':
            return []
        else:
            def F(c):
                if len(c) == 1:
                    return d[c]
                else:
                    f = []
                    for x in d[c[0]]:
                        for y in F(c[1:]):
                            f += [x + y]
                    return f
            return F(digits)

class Solution(object):
    def letterCombinations(self, digits):
        if digits == '':
            return []
        d = {
        '2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',
        }
        def F(c):
            if len(c) == 1:
                return d[c]
            else:
                f = []
                for x in d[c[0]]:
                    for y in F(c[1:]):
                        f += [x + y]
                return f
        return F(digits)