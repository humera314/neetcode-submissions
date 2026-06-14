class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hm=defaultdict(list)
        for char in strs:

            sort_key=''.join(sorted(char))

    
            hm[sort_key].append(char)
        return list(hm.values())

        