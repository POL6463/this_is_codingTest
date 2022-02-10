input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

count = 0
for i in range(1, 3):
    if row + i <= 8:
        count += 1
    if row - i >= 1:
        count += 1
    if column + i <= 8:
        count += 1
    if column - i >= 8:
        count += 1

print(count)