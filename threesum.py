class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums = sorted(nums)
        i = 0
        n = len(nums)
        result = []
        
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
    
            j = i + 1
            k = n - 1

            while j < k:
                r = nums[i] + nums[j] + nums[k]
                if r == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    
                    while j < n-1 and nums[j] == nums[j + 1]:
                        j += 1
                    
                    while k > 0 and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

                if r < 0:
                    j += 1
                
                if r > 0:
                    k -= 1
            
    
    
        return result

s = Solution()
# print(s.threeSum([1,2,-2,-1]))
print(s.threeSum([0,0,0]))

            
            
        