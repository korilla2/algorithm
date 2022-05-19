# 8 queens
n = 8

# 정답의 갯수
cnt = 0

# 각 depth 들의 값 저장할 배열
arr = [None] * n

# 바로 위, 왼쪽 위 대각선, 오른쪽 위 대각선 검사


def check(a):
    for i in range(a):
        '''
        i는 a 전의 깊이를 의미
        방금 퀸을 놓은 깊이 이전 깊이까지만 찾아보며 검사를 진행
        현재 말을 놓은 위치는 arr[a] 를 의미
        여기서 arr[i]는 이전깊이들에 존재하는 값을 의미
        arr[a] == arr[i] 라는 것은 내가 현재 놓은 위치의 값이 이미 저장되어 있다는 뜻
        그 말은 같은 열에 이미 퀸을 놓았다는 뜻이고 세로줄을 의미

        각 층마다 말을 놓아가면서 진행하므로 어떠한 경우에든 밑에 대각선은 존재하지 않음
        그래서 왼쪽 위, 오른쪽 위 대각선만 검사하면 되는데,
        현재 놓은 곳의 값(arr[a]) 에서 이전에 놓아진 값(arr[i])과의 차이가 
        현재 깊이(a) 에서 이전깊이(i) 까지의 차이의 절대값이 동일함을 이용
        '''
        #      바로 위쪽 검사                   대각선 검사
        if (arr[a] == arr[i]) or (abs(arr[a] - arr[i]) == abs(a - i)):
            return False
    return True

# 퀸을 놓는 재귀함수


def queens(a):
    global cnt

    # 최대 깊이까지 도달하면 다 찾았다는 의미로 정답의 갯수를 1 늘려줌
    if a == n:
        cnt += 1

    # 각 깊이마다 0부터 7까지 값을 놓아가며 진행
    # check 함수를 통과하면 다음 깊이로 재귀
    else:
        for i in range(n):
            arr[a] = i
            if check(a):
                queens(a+1)


queens(0)
print(cnt)
