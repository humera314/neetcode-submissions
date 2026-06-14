class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        count=0

        for n in nums:
            if n-1 not in num_set:
                cur_num=n
                cur_streak=1

                while cur_num+1 in num_set:
                    cur_num+=1
                    cur_streak+=1
                
                count=max(count,cur_streak)
        return count
                
