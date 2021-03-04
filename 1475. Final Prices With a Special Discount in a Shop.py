class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        output = []
        original_price = 0
        discount = 0
        for i in range(len(prices)-1):
            original_price = prices[i]
            for j in range(i+1,len(prices)):
                if prices[i] >= prices[j]:
                    discount = prices[j]
                    break
                else:
                    discount = 0
            final_price = original_price - discount
            output.append(final_price)
        output.append(prices[-1])
        return output
        