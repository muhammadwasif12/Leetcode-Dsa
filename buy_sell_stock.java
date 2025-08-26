public class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int price : prices) {
            // Update the minimum price so far
            if (price < minPrice) {
                minPrice = price;
            }
            // Calculate the potential profit
            int profit = price - minPrice;
            // Update the maximum profit found so far
            if (profit > maxProfit) {
                maxProfit = profit;
            }
        }

        return maxProfit;
    }
}


public class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;

        // Iterate through each day as buy day
        for (int i = 0; i < prices.length; i++) {
            // Iterate through each day after the buy day as sell day
            for (int j = i + 1; j < prices.length; j++) {
                // Calculate the profit by selling on the jth day after buying on ith day
                int profit = prices[j] - prices[i];
                // Update maxProfit if this profit is greater than seen before
                if (profit > maxProfit) {
                    maxProfit = profit;
                }
            }
        }

        return maxProfit;
    }
}