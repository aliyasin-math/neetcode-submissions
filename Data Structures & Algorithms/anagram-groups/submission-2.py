class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
                
        myMap = {}
        for i in range(len(strs)):
            key = tuple(sorted(strs[i]))
            if key in myMap:
                myMap[key].append(strs[i])
            else:
                myMap[key] = [strs[i]]

        return list(myMap.values())
            
