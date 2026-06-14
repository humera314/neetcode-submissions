class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        res = []
       


        for num, value in freq.items():
            res.append((value, num))
        res.sort(reverse=True)
        arr = []
        for i in range(k):
            arr.append(res[i][1])
        return arr

        