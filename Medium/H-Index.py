class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        num_citations = [0] * (n+1)
        for nums in citations:
            if nums >= n:
                num_citations[n] += 1
            else:
                num_citations[nums] += 1
        papers = num_citations[n]
        h = n
        while papers < h:
            papers += num_citations[h-1]
            h -=1
        return h
        
