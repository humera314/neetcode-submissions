class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm = defaultdict(list)

        for char in strs:
            sortx=''.join(sorted(char))
            
            hm[sortx].append(char)
        return list(hm.values())
        