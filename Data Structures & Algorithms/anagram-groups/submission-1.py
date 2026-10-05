class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = []
        for n in strs:
            strs_sorted.append(sorted(n))
        
        myMap = {}
        for i in range(len(strs)):
            key = tuple(strs_sorted[i])
            if key in myMap:
                myMap[key].append(strs[i])
            else:
                myMap[key] = [strs[i]]

        return list(myMap.values())
            
