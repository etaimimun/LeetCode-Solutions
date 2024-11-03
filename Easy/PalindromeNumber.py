class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        testString = ''
        for char in str(x):
            stack.append(char)
        while stack != []:
            testString += stack.pop()
        if testString == str(x):
            return True
        return False