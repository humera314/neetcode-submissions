class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicts={}
        for i  in range(len(nums)):
            diff=target-nums[i]
            if diff in dicts:
                return [dicts[diff],i]
            else:
                dicts[nums[i]]=i


                