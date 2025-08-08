T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    sum_arr = []
    for i in range(N):
        for j in range(N):
            sum = arr[i][j]
            for x, y in zip(dx, dy):
                ni = i+x
                nj = j+y
                if ni<0 or nj<0 or ni>=N or nj >= N:
                    continue
                else:
                    sum += arr[ni][nj]
        sum_arr.append([sum, i ,j])
    result = sorted(sum_arr, key=lambda x: (x[0], -x[1], -x[2]))
    print(f"#{test_case} {' '.join(map(str,result[-1]))}")
