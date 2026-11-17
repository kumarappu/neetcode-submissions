class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) -1
        s = s.upper()
        while l < r and l < len(s) and r >=0:
            while l<len(s) and not s[l].isalnum():
                l+=1
            while r>=0 and not s[r].isalnum():
                r-=1
            if l < len(s) and r >=0 and s[l] != s[r]:
                return False
            l=l+1
            r=r-1
        
        return True;