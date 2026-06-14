class Solution:

    def encode(self, strs: List[str]) -> str:

        res=''
        for char in strs:
            res+=str(len(char))+'#'+char
           
        return res


    def decode(self, s: str) -> List[str]:
        left= 0
        res=[]
        while left < len(s):
            right=left
            while s[right]!='#':
                right+=1

            leng=int(s[left: right])

            left=right+1 # 1st char
            right=left +leng
            res.append(s[left:right])
            left=right
        return res
            
        
     
            

