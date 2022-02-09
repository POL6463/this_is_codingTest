n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin #몫만 반환은 // 두개
    n %= coin

print(count)
