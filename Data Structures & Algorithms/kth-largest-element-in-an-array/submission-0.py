class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        n=len(nums)
        val=[]
        print(heapq.nlargest(k, nums))
        return heapq.nlargest(k, nums)[-1]
        