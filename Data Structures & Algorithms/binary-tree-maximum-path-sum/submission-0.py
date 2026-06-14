# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res= [root.val]
        
        
        def dfs(node):
            if not node:
                return 0
           
            
            LM=dfs(node.left)
            #sums.append(node.val)
            RM=dfs(node.right)
            LM=max(LM, 0)
            RM=max(RM,0)

            res[0]=max(res[0], node.val+ LM+ RM)
            return node.val + max(LM, RM)
            
        dfs(root)
        return res[0]


        