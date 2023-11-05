class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        
        
        
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)

        return False


s = Solution()

print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
