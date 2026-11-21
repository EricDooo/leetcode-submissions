class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left: int, right: int) -> tuple[int, int]:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # The pointers have moved one step past the palindrome.
            return left + 1, right

        best_start = best_end = 0

        for center in range(len(s)):
            for right in (center, center + 1): # Even and Odd centers palindrome
                start, end = expand(center, right)
                if end - start > best_end - best_start:
                    best_start, best_end = start, end

        return s[best_start:best_end]