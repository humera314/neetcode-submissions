class Solution:
    def isPalindrome(self, s: str) -> bool:
        

        filter_s=''.join(char.lower() for char in s if char.isalnum())
        l,r= 0, len(filter_s)-1
        print(f"Filtered string: {filter_s}")  # Debugging line
        while l<r:
            #print(f"Filtered string: {filter_s[r]}")  # Debugging line
            if filter_s[l] != filter_s[r]:
                return False
            l+=1
            r-=1

        return True

        

        
        