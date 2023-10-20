class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        i = 0
        j = 1
        k = 2
        new_nums = []
        len_nums = len(nums)

        if len(set(nums)) == 1 and sum(nums) == 0:
            return [[nums[i],nums[j],nums[k]]]

        while i < len_nums:

            if j > len_nums -1:
                i += 1
                j = i + 1
                k = j + 1
                continue

            if k > len_nums - 1:
                j += 1
                k = j + 1
                continue

            r = nums[i] + nums[j] + nums[k]
            if r == 0:
                
                nw = len(new_nums)
                z = 0
                r = True
                
                while z < nw:
                    if nums[i] in new_nums[z] and nums[j] in new_nums[z] and nums[k] in new_nums[z]:
                        if nums[i] == 0 and nums[j] == 0 and nums[k] == 0:
                            z += 1
                            continue
                        r = False
                    z += 1

                if [nums[i] , nums[j] , nums[k]] in new_nums:
                    k += 1
                    continue
                
                if r:
                    new_nums.append([nums[i] , nums[j] , nums[k]])

            k += 1

        return new_nums

s = Solution()
print(s.threeSum([4,4,3,-5,0,0,0,-2,3,-5,-5,0]))
            
            
        