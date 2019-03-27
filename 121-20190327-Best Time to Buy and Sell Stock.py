class Solution:
    def besttimetobuyandsell(self,prices):
        max_profit,min_price=0,float('inf')
        for price in prices:
            min_price=min(price,min_price)
            profit=price-min_price
            max_profit=max(max_profit,profit)
        return max_profit


S=Solution()
print(S.besttimetobuyandsell([1,2,3,4,5,6,7,6,8,9,2,4,7,4,10]))