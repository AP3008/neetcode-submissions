class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
       # We can use Bellman-Ford, which can also deal with negative nodes

        # We store all of the prices as infinity to start and since the nodes are labeled from 0 -> n-1 we can use the list like this
        prices = [float("inf")] * n
        # The source node will always have no cost 
        prices[src] = 0

        # We want to loop k+1 times, because at minimum we need to travel at least one path. Also this effectivley simulates our BFS esque algorithim, looping only k times so we can see the best solution we can get in k iterations.
        for i in range(k+1):
            # we store a tmp of the prices in a tmp list 
            tmpPrices = prices.copy()

            # We take the flights which we have 
            # s = from_i = where we are flying from 
            # d = to_i = destination
            # p = price_i = price of the flight
            for s, d, p in flights:
                # If the price at this source is labeled infinity in our general prices list, that means we haven't seen any flights from somewhere we have visited to this place, so we skip over it for now 
                if prices[s] == float("inf"):
                    continue 
                # Since we know that this source has a cost associated with reaching it 
                # We want to check if the price of getting to the src + the price of the flight is less than whatever value is stored in tmp[destination]. If it is we want to store this as the cheapest way to get to this destination  
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            # At the end of going through each flight we want to update the prices to reflect the changes made in tmpPrices 
            prices = tmpPrices
        # If our destination was updated to some cost we will return that, it may not be the cheapest way but it si within k stops. If we could not find a way there in k stops we return -1 
        return -1 if prices[dst] == float("inf") else prices[dst]
            