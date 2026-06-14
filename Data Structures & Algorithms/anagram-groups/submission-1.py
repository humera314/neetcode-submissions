class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        dicts={}
    
        for s in strs:
            sortedS="".join(sorted(s))   #Input: ['a', 'e', 't'] Output: "aet" (a single sorted string).
            if sortedS not in dicts:
                dicts[sortedS]=[s]
            else:
                dicts[sortedS].append(s)

        return list(dicts.values())


        #TC N SC NlogN