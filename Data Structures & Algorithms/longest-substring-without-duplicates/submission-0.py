class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        count=0
        res=0
        l=0
        for r in range(len(s)):
            while s[r] in seen:
                count-=1
                seen.remove(s[l])
                l+=1
                
          
            seen.add(s[r])
            count+=1
            res=max(res,count)

        return res        