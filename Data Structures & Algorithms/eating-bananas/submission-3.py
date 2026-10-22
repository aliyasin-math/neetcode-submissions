class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        while l<r:
            mid = (r+l)//2
            hours = sum((pile+mid-1)//mid for pile in piles)
            
            if hours <= h:
                r = mid
            elif hours > h:
                l = mid+1
        return l
        