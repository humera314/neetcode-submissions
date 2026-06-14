class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)

        for char in strs:
            sort_char=''.join(sorted(char))

            res[sort_char].append(char)
            
            
        return list(res.values())
        

        