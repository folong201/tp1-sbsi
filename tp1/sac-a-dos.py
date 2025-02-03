def knapsack(valeurs, poids, W):
    n = len(valeurs)
    dp = [[0] * (W + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(W + 1):
            if poids[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], valeurs[i - 1] + dp[i - 1][w - poids[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][W]


valeurs = [60, 100, 120]
poids = [10, 20, 30]
W = 50
print("Valeur maximale obtenue :", knapsack(valeurs, poids, W))
#Valeur maximale obtenue : 220