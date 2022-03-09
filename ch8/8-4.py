#피보나치 수열 바텀업
DP = [0] * 100

DP[1] = 1
DP[2] = 1
n = 99

for i in range(3, n + 1):
    DP[i] = DP[i-1] + DP[i-2]

print(DP[n])