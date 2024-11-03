class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        string1 = s1.split()
        string2 = s2.split()
        commonWords = []
        allWords = {}
        uncommonWords = []
        for words in string2:
            if words in allWords:
                allWords[words] += 1
            else:
                allWords[words] = 1
        for words in string1:
            if words in allWords:
                allWords[words] += 1
            else:
                allWords[words] = 1
            if words in string2:
                commonWords.append(words)
        for words in allWords:
            instance = allWords[words]
            if allWords[words] > 1:
                #for i in range(1, my_dict['count'] + 1)
                for i in range (1, allWords[words] + 1):
                    commonWords.append(words)
        uncommonWords = s1.split() + s2.split()
        #uncommonWords = uncommonWords - commonWords
        for words in commonWords:
            if words in uncommonWords:
                uncommonWords.remove(words)

        return uncommonWords

            
            