class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        currentChars = set()
        currentLongest = 0
        while r < len(s):

            if s[r] in currentChars:
                currentChars.remove(s[l])
                l += 1
            else:
                currentChars.add(s[r])
                currentLongest = max(currentLongest, len(currentChars))
                r += 1
        return currentLongest