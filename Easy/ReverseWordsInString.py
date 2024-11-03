class Solution:
    def reverseWords(self, s: str) -> str:
        new_string = ""
        current_word = []
        for char in s:
            if char == " ":
                current_word.reverse()
                for char in current_word:
                    new_string += char
                new_string += " "
                current_word.clear()
            else:
                current_word.append(char)
        current_word.reverse()
        for char in current_word:
            new_string += char
        return new_string