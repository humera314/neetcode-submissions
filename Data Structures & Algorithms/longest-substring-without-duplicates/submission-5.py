class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        i, j=0,0
        seen=set()
        maxlen=0
        count=0
        while j< len(s):

            while s[j]  in seen:
                seen.remove(s[i])
                i+=1

              
            seen.add(s[j])   
            j+=1
         
            
            print(seen, count)
            maxlen= max(maxlen,j-i)
                
                
        
        return maxlen

        