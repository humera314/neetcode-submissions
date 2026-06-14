class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm={}
        i,j=0,0
        maxi, maxi_wind=0,0
        while j< len(s):
            
            hm[s[j]]=hm.get(s[j],0)+1

            maxi=max(hm[s[j]], maxi)

            if (j-i+1)-maxi> k:
                hm[s[i]]-=1
                i+=1
                

            maxi_wind=max(j-i+1, maxi_wind)

            j+=1    
        return maxi_wind
        