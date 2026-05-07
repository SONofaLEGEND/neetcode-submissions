class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        arr = []
        # {1:0,2:0,3:0}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # {1:1, 2:2, 3:3}
        for n, c in count.items():
            arr.append([c,n])
        arr.sort()
        # [[1,1],[2,2],[3,3]]

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res

        