class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}

        for n in nums:
            if n in dic:
                return True
            else:
                dic[n]=True  # using dic[key] = value.
        return False
                
                
         