class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) ==0:
            return [[""]]
        lookup = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            lookup.setdefault(sorted_str , []).append(s)

        
        subsets = []
        for subset in lookup.values():
            subsets.append(subset)
        
        return subsets
        