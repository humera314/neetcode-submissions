class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        def backtrack(i,cur, target):
            
            if target<0 or i==len(nums):
                return
            if target==0:
                return res.append(cur.copy())

            
            cur.append(nums[i])
            backtrack(i,cur, target-nums[i])
            cur.pop()
            backtrack(i+1, cur, target)
        
        backtrack(0,[],target)

        return res