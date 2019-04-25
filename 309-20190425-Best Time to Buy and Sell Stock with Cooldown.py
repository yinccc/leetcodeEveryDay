class Solution:
    def bestTime(self,price):
        hold,sold,rest=float("-inf"),0,0
        for p in price:
            hold,sold,rest=max(hold,rest-p),hold+p,max(rest,sold)
        return max(sold,rest)
