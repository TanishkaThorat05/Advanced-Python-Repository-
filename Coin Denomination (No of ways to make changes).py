# Number of Ways to Make Change using Dynamic Programming

# Accept coin denominations
coins = list(map(int, input("Enter coin denominations: ").split()))

# Accept target amount
target = int(input("Enter target amount: "))

# DP array
dp = [0] * (target + 1)

# There is 1 way to make amount 0: choose no coins
dp[0] = 1

# Calculate number of combinations
for coin in coins:
    for amount in range(coin, target + 1):
        dp[amount] += dp[amount - coin]

# Display result
print("Total possible combinations:", dp[target])
