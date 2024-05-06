def greedyChange(coinSet, N):
    if N == 0:
        return 0

    coins = float('inf')

    for coin in coinSet:
        if N - coin >= 0:
            res = greedyChange(coinSet, N - coin)
            if res != float('inf'):
                coins = min(coins, res + 1)

    return coins

if __name__ == "__main__":
    coinSet = [1, 5, 10, 15, 20]
    N = 27
    print("El mínimo de monedas para dar cambio es:", greedyChange(coinSet, N))
