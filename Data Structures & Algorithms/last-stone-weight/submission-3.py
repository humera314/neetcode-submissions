class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st=[]
        for stone in stones:
            heapq.heappush(st, -stone)


        while len(st)>1:
            f=heapq.heappop(st)
            s= heapq.heappop(st)     
            heapq.heappush(st, (f-s))
        
            
        return -st[0] 



        