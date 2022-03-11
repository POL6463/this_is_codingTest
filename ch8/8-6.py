n = int(input())

array = list(map(int, input().split()))
DP = [0] * 100

DP[0] = array[0]
DP[1] = max(array[0], array[1])
for i in range(2, n):
    DP[i] = max(DP[i-1], DP[i-2] + array[i])

print(DP[n-1])
