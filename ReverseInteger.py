class Solution:
    def reverse(self, x: int) -> int:

        if x == 0 and x < -2**31 or x > 2**31 - 1:
            return x

        x = str(x)
        l_x = len(x)
        new_x = []
        
        for i in range(l_x-1,-1,-1):
            if len(new_x) == 0 and x[i] == "0":
                continue
            if x[i].isdigit():
                new_x.append(x[i])
        
        if x[0] == "-":
            new_x.insert(0,"-")
        
        x = int("".join(new_x))
        
        if x < -2**31 or x > 2**31 - 1:
            return 0
        
        return x

s = Solution()
print(s.reverse(1534236469))

print(1534236469 > (2**31 - 1),2**31)