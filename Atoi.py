class Solution:
    def myAtoi(self, s: str) -> int:

        assing = 0
        number = ""
        index = 0

        while index < len(s):
            
            if s[index] == " " and len(number) == 0 and assing == 0:
                index += 1
                continue
            elif s[index] == "-" and assing == 0 and len(number) == 0:
                assing = -1
            elif s[index] == "+" and assing == 0 and len(number) == 0:
                assing = 1
            elif s[index].isdigit():
                number += s[index]
            else:
                break

            index += 1

        if len(number) < 1:
            return 0

        if assing == 0:
            assing = 1

        xs = int(number) * assing
        
        limit_low = -2**31
        limit_hight = 2**31 -1
        
        if xs < limit_low:
            return limit_low
        elif xs > limit_hight:
            return limit_hight

        return xs


s = Solution()
print(s.myAtoi("  +  413"))
