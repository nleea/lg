class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        
        resulst = 0
        
        while l < r:
            resulst = max(resulst,min(height[l],height[r]) * (r - l))
            
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        
        return resulst

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
        