n, m, k = map(int, input().split())
#  8, 3
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n -2]

count = int(m / (k + 1)) * k #가장 큰 수를 몇번이나 곱해야 하는지 계산
print("count : " +  str(count))
count += m % (k+1)
print("count : " +  str(count))


result = 0
result += (count) * first
result += (m - count) *second
print(result)