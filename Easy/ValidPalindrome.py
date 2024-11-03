class Solution:
    def isPalindrome(self, s: str) -> bool:
        #two pointers, left and right. R == len(s), L = 0
        #if s[r] == s[l], keep going, R -= 1, L  += 1: else return false
        #if R == L return true
        #first have to remove spaces and puncuation
        cleanString = ''
        for char in s:
            if char.isalnum():
                cleanString += char.lower()
        if len(cleanString) == 0 or len(cleanString) == 1:
            return True
        #print(cleanString)
        l = 0 
        r = len(cleanString) - 1
        while l < r:
            #print(l, r)
            if cleanString[l] != cleanString[r]:
                return False
            l += 1
            r -= 1
        return True
        

        