class Solution(object):
    def distributeCandies(self, candies):
        # Note:
        #   return "Number of different values" > "Subarray length" ? 
        #     "Subarray length" : "Number of different values"
        #
        #   //: divide with integral result (discard remainder)
        return min(len(set(candies)), len(candies)//2)