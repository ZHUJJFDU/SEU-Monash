def mincostTickets(days, costs):
    # DP array to store minimum cost up to day i
    dp = [0] * 366  # We need to calculate for all days from 1 to 365
    
    travel_set = set(days)  # Convert days to a set for O(1) lookups
    
    # Iterate over each day from 1 to 365
    for i in range(1, 366):
        if i not in travel_set:
            dp[i] = dp[i-1]  # No travel on this day, cost remains the same
        else:
            # Calculate the cost if we buy a 1-day, 7-day, or 30-day pass
            dp[i] = min(
                dp[i-1] + costs[0],  # One-day pass
                dp[max(0, i-7)] + costs[1],  # Seven-day pass
                dp[max(0, i-30)] + costs[2]  # Thirty-day pass
            )
    
    # The answer will be the minimum cost to travel through all the days
    return dp[365]

def solve():
    t = int(input())  # Number of test cases
    
    for _ in range(t):
        m = int(input())  # Number of days
        days = list(map(int, input().split()))  # List of days on which you travel
        costs = list(map(int, input().split()))  # List of costs for 1-day, 7-day, 30-day tickets
        
        # Find the minimum cost for this test case
        result = mincostTickets(days, costs)
        
        # Output the result for the test case
        print(result)

# Call the solve function to process the input and output the result
solve()
