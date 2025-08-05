T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    # n_list = []
    # for i in range(N):
    #      n_list.append(list(map(int, input().split())))
    n_list = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    # c_j_list = []
    # for i in range(P):
    #     c = int(input())
    #     c_j_list.append(c)
    c_j_list = [int(input()) for _ in range(P)]

    # dat 만들기
    count_list = [0] * 5001
    for i in range(len(n_list)):
        for j in range(n_list[i][0],n_list[i][1]+1):
            count_list[j] += 1

    # dat 써서 출력
    print(f'#{test_case}', end = ' ')
    for i in c_j_list:
        print(f'{count_list[i]}', end= ' ')
    print()