class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = [[[]]] + [[]] * target
        for c in candidates:
            for j in range(1, target + 1):
                if j >= c:
                    dp[j] = dp[j] + list(map(lambda x: x + [c], dp[j - c]))

        return dp[target]


s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
