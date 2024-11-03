class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''
        list = []
        for item in digits:
            string += str(item)
        string = int(string) + 1
        for char in str(string):
            list.append(int(char))
        return list
            