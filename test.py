cnt = 0

temp = dict()

temp[0] = 2
temp[1] = 3


ptr = 2

for n in range(5, 1001, 2):
    i = 1
    while temp[i] ** 2 <= n:
        cnt += 2
        if n % temp[i] == 0:
            break
        i += 1

    else:
        temp[ptr] = n
        ptr += 1
        cnt += 1
print(cnt)
print(temp)
