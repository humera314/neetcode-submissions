class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sortS=sorted(s)
        sortT=sorted(t)
       
        if len(sortS)!=len(sortT):
            return False
        for l in range(len(s)):
            if sortS[l]!=sortT[l]:
               return False
        return True

        