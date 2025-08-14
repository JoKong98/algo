T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, P = map(int, input().split())
    virus_arr = [[*map(int, input().split())] for _ in range(N)]
    max_count = 0
    for i in range(N):
        for j in range(N):
            count = virus_arr[i][j]
            for k in range(1,P+1):
                if i-k>=0:
                    count += virus_arr[i-k][j]
                if i+k <=N-1:
                    count += virus_arr[i+k][j]
                if j+k <= N-1:
                    count += virus_arr[i][j+k]
                if j-k >= 0:
                    count += virus_arr[i][j-k]
            if max_count < count:
                max_count = count
                        
    print(f'#{test_case} {max_count}')