DP = [0] * 30005

DP[1] = 1
DP[2] = 1
DP[3] = 1
DP[5] = 1

x = int(input())

for i in range(6, x + 1):
    if(i % 5 == 0):
        DP[i] = 1 + DP[i//5]
    elif(i % 3 == 0):
        DP[i] = 1 + DP[i//3]
    elif(i % 2 == 0):
        DP[i] = 1 + DP[i//2]
    else:
        DP[i] = 1 + DP[i-1]


print(DP[i])