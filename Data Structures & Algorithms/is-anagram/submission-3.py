class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!=len(t):
            return False
        hm_count={}
        hm_count1={}
        for c in range(len(s)):
            hm_count[s[c]]=hm_count.get(s[c],0)+1
            hm_count1[t[c]]=hm_count1.get(t[c],0)+1

        if hm_count==hm_count1:
            return True
        return False
        
    
        
        
        