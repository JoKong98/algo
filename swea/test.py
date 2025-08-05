T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////

    h, w =  map(int, input().split())
    li_a = []
    for i in range(h):
        li_a.append(list(map(int, input().split())))

    g_count = 0
    b_count = 0
    dic_b = {}
    li_b = []
    b_h, b_w = map(int, input().split())
    for i in range(b_h):
        li_b.append(list(map(int, input().split())))
        for j in range(b_w):
            dic_b[li_b[i][j]] = 1
    for i in range(h):
        for j in range(w):
            if li_a[i][j] in dic_b.keys():
                b_count += 1
            else:
                g_count += 1
                continue

    print(f'#{test_case} {b_count} {g_count}')
# ///////////////////////////////////////////////////////////////////////////////////