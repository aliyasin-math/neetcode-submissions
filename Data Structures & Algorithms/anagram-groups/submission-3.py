class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for n in strs:
            key = "".join(sorted(n))
            myMap[key].append(n)
        return list(myMap.values())