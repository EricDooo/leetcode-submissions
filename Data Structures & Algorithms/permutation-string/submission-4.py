class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1) - 1

        counts1 = [0] * 26
        for c in s1:
            counts1[ord(c) - ord('a')] += 1

        counts2 = [0] * 26
        for i in range(len(s1)):
            counts2[ord(s2[i]) - ord('a')] += 1

        while r < len(s2) - 1:
            if counts1 == counts2:
                return True
            counts2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            counts2[ord(s2[r]) - ord('a')] += 1

        return counts1 == counts2