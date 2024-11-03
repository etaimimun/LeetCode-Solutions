class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringAsList = s.split()
        length = 0
        lastElement = len(stringAsList) - 1
        for char in stringAsList[lastElement]:
            length += 1
        return length