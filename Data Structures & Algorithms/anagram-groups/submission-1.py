from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashset = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            hashset[sortedS].append(s)
        return list(hashset.values())


        