class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #put all letters in a map, with "char: number of times it pops up"
        charMap = defaultdict(int)
        # if len(s) != len(t):
        #     return False
        for char in s:
                charMap[char] += 1
        for char in t:
            charMap[char] -= 1
        for val in charMap.values():
            if val != 0:
                return False
        return True