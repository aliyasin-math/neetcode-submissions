class Solution:
    def isValid(self, s: str) -> bool:
        items = list(s)

        if len(items)%2 == 1:
            return False
        elif items == []:
            return True
        
        while len(items) != 0:
            for i in range(len(items)-1):
                if (items[i] == "(") and (items[i+1] == ")"):
                    del items[i:i+2]
                    break
                if (items[i] == "{") and (items[i+1] == "}"):
                    del items[i:i+2]
                    break
                if (items[i] == "[") and (items[i+1] == "]"):
                    del items[i:i+2]
                    break
            else:
                return False
        return True
            

                    



