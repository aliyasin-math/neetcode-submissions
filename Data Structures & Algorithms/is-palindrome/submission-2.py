class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s)
        temp = []

        for n in s:
            if n.isalnum() == True:
                temp.append(n.lower())
                
        for i in range(len(temp)):
            if temp[i] == temp[len(temp)-i-1]:
                continue
            else:
                return False
        return True