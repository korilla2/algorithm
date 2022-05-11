result = dict()

result[0] = 2
result[1] = 3

cnt = 2

for i in range(5, 13, 2):
    k = 1
    while result[k] ** 2 <= i:
        if i % result[k] == 0:
            break
        k += 1

    else:
        result[cnt] = i
        cnt += 1
print(*result.values())
