temp = dict()

temp[0] = 2
temp[1] = 3

cnt = 2

# 5부터 홀수만 선택
for i in range(5, 101, 2):
    k = 1

    # 찾아낸 소수의 제곱 이하의 범위 판별
    while temp[k] ** 2 <= i:

        # 나누어 떨어지면 소수 아님
        if i % temp[k] == 0:
            break

        # 다음번 소수로 비교
        k += 1

    # 소수 추가
    else:
        temp[cnt] = i
        cnt += 1

print(temp)
