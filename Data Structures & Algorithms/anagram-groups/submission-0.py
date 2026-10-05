class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myMap = {}
        for n in strs:
            key = tuple(sorted(n))
            if key in myMap:
                myMap[key].append(n)
            else:
                myMap[key] = [n]

        return list(myMap.values())