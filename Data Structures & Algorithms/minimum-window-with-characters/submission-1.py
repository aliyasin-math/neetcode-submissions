class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        myMap1 = {}
        for n in t:
            myMap1[n] = 1 + myMap1.get(n, 0)
        
        myMap2 = {}
        l = 0
        start, length = 0, len(s) + 1
        matches, need = 0, len(myMap1)

        for r in range(len(s)):
            if s[r] in myMap1: 
                myMap2[s[r]] = 1 + myMap2.get(s[r], 0)
                if myMap2[s[r]] == myMap1[s[r]]:
                    matches += 1
            
            while matches == need:
                if r-l+1<length:
                    length = r-l+1
                    start = l
                if s[l] in myMap1:
                    myMap2[s[l]] -= 1
                    if myMap2[s[l]] < myMap1[s[l]]:
                        matches -= 1
                l += 1

        return "" if length == len(s)+1 else s[start:length+start]


