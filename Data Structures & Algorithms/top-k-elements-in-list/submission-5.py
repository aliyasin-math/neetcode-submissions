class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        res = []

        for n in nums:
            myMap[n] = 1 + myMap.get(n,0)
        for i in range(k):
            key = max(myMap, key=myMap.get)
            res.append(key)
            myMap.pop(key)
        return res

        