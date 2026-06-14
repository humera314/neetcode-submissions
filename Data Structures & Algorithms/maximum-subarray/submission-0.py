class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum=  max_num=nums[0]
        for num in nums[1:]:
            curSum=max(num, curSum+num)
            max_num=max(curSum, max_num)
        return max_num
