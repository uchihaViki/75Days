class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        l, r = 0, 1
        ans = 0
        while r < len(prices):
            ans = max(ans, prices[r]-prices[l])
            if prices[l] > prices[r]:
                l = r
            r += 1
        return ans
            