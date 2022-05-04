class Solution:
    def intToRoman(self, n: int) -> str:
        num = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        r=''
        while n:
            for i in range(len(num)):
                if n>=num[i]:
                    r+=sym[i]
                    n-=num[i]
                    break
        return r