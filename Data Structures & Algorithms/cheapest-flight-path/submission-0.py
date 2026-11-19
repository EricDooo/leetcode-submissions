class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1): # k + 1 is how many edges we create, meaning 1 stop
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"): # skip infs
                    continue
                if prices[s] + p < tmpPrices[d]: # tmpPrices[d] = min(tmpPrices[d], prices[s] + p)
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        return -1 if prices[dst] == float("inf") else prices[dst] # If dst is unreachable in k+1