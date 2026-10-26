class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False   

        myMap1 = {}

        for i in range(len(s1)):
            myMap1[s1[i]] = 1 + myMap1.get(s1[i], 0)
        
        myMap2 = {} 
        l = 0

        for r in range(len(s2)):
            if r-l+1>len(s1):
                myMap2[s2[l]] -= 1
                if myMap2[s2[l]] == 0:
                    myMap2.pop(s2[l])
                l += 1
            myMap2[s2[r]] = 1 + myMap2.get(s2[r], 0)
            if (r-l+1==len(s1)) and (myMap1 == myMap2):
                return True
            print(myMap1, myMap2, l,r)
        return False
            


