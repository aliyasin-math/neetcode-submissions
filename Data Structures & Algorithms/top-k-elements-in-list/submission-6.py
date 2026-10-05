class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myMap = {}
        res = []

        for n in nums:
            myMap[n] = 1 + myMap.get(n,0)
        
        return sorted(myMap, key = myMap.get, reverse=True)[:k]

        