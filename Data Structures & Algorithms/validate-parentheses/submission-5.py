class Solution:
    def isValid(self, s: str) -> bool:
        items = list(s)

        stack  = []
        myMap = {")" : "(", "}" : "{", "]" : "["}

        for n in items:
            if n in myMap:
                if len(stack) != 0 and myMap[n] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(n)
        return len(stack) == 0

        

                    



