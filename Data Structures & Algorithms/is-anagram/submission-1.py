class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_lookup = {}
        for char in s:
            s_lookup[char] = s_lookup.get(char, 0) +1
        
        t_lookup = {}
        for char in t:
            t_lookup[char] = t_lookup.get(char, 0) +1
        
        if len(s_lookup) != len(t_lookup):
            return False
        
        for key,value in s_lookup.items():
            if t_lookup.get(key,0) != value:
                return False
        
        return True
        

        