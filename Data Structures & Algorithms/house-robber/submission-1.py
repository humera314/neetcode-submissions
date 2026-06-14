class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp=[0]* len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for n in range(2,len(nums)):
            
            dp[n]=max(dp[n-1],(nums[n]+dp[n-2]))
        return dp[-1]


        