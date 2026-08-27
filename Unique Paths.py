# Unique Paths Problem using Dynamic Programming

# Accept number of rows and columns
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

# Create DP table
dp = [[0] * columns for _ in range(rows)]

# First row and first column have only one possible path
for i in range(rows):
    dp[i][0] = 1

for j in range(columns):
    dp[0][j] = 1

# Calculate unique paths
for i in range(1, rows):
    for j in range(1, columns):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

# Display result
print("Total number of unique paths:", dp[rows - 1][columns - 1])
