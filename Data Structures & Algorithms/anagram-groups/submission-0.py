class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        dicts={}
    
        for s in strs:
            sortedS="".join(sorted(s))
            if sortedS not in dicts:
                dicts[sortedS]=[s]
            else:
                dicts[sortedS].append(s)

        return list(dicts.values())