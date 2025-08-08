T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, m = map(int, input().split())
    fly_list = [[*map(int, input().split())] for _ in range(N)]
    # max_count = 0
    # count = 0
    # for i in range(N-m):
    #     for j in range(N-m):
    #         count = 0
    #         for x in range(m):
    #             count += sum(fly_list[i + x][j:j + m])  # 가로로 m개씩 m행 반복
    #         if max_count < count:
    #             max_count = count
    # print(max_count)
    max_count = max(
        sum(sum(row[j:j+m]) for row in fly_list[i:i+m])
        for i in range(N-m+1)
        for j in range(N-m+1)
    )
    print(f'#{test_case} {max_count}')