class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
        result = ""

        while num !=0:
                for key in d:
                    if key<=num or key==1:
                        div = num // key
                        for _ in range(div):
                            result = result + d[key]
                        num = num % key

        return result

s = Solution()
print(s.intToRoman(899))