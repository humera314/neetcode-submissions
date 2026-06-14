class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq=Counter(nums) #Counter(nums)=1:3, 2:4....

        sorted_element=sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

        return sorted_element[:k]