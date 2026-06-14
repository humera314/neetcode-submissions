class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
        max_cnt=0
        seen=set(nums)
        for num in nums:
            count=1

            while num-1 in seen:
                count+=1
                num=num-1
            max_cnt=max(max_cnt, count)
        return max_cnt

        