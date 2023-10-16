class Solution:
    def convert(self, s: str, numRows: int) -> str:
        t = True
        new_s = []
        index = 0
        
        if numRows == 1:
            return s
        
        for i in range(len(s)):
            if i < numRows:
                new_s.append([s[i]])
                index += 1
                continue

            if index == 1 and t == False:
                t = True
            
            if index == numRows and t == True:
                t = False
            
            if t:
                new_s[index].append(s[i])
                index += 1
            else:
                index -= 1
                new_s[index-1].append(s[i])
        s = ""
        for i in new_s:
            s += "".join(i)
        return s
        
s = Solution()
print(s.convert("ABC",1))