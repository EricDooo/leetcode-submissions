class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx = 0
        resLen = 0

        for i in range(len(s)):
            # odd length
            resIdx, resLen = self.isPalindrome(i,i,s, resIdx, resLen)
            # even length
            resIdx, resLen = self.isPalindrome(i,i+1,s, resIdx, resLen)

        return s[resIdx : resIdx + resLen]
        
    def isPalindrome(self, l: int, r: int, s: str, resIdx, resLen) -> list:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    resIdx = l
                    resLen = r - l + 1
                l -= 1
                r += 1
            return [resIdx, resLen]
