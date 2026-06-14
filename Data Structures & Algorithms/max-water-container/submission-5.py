class Solution:
    def maxArea(self, heights: List[int]) -> int:


    
        max_area=0
        leng, bred=0,0
        for left in range(len(heights)):
            right=left+1
            while right<len(heights):

                leng= min(heights[left], heights[right])
                bred= right-left

                max_area= max(max_area, leng* bred)
                right+=1
            
        return max_area
        