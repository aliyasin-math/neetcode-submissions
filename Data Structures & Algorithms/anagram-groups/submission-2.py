class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = defaultdict(list)
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            myMap[key].append(strs[i])

        return list(myMap.values())