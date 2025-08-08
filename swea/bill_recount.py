T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number_list = list(map(int, input().split()))
    dt = [0] * (N+1)
    J = int(input())
    for _ in range(J):
        s, f, v = map(int, input().split())
        dt[s] += v
        dt[f+1] -= v
    current_dt = 0
    for i in range(N):
        current_dt += dt[i]
        number_list[i] += current_dt

    # print(f'#{test_case}', end = ' ')
    # for i in range(len(number_list)):
    #     print(f'{number_list[i]}', end= ' ')
    # print()
    print(f"#{test_case} {' '.join(map(str, number_list))}")