for test_case in range(1, 11):
    N = int(input())  # 일반적으로 100
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    for i in range(100):
        max_sum = max(max_sum, sum(arr[i][j]for j in range(100)))

    for j in range(100):
        max_sum = max(max_sum, sum(arr[i][j]for i in range(100)))


    main_diag = sum(arr[i][i] for i in range(100))
    max_sum = max(max_sum, main_diag)

    anti_diag = sum(arr[i][99 - i] for i in range(100))
    max_sum = max(max_sum, anti_diag)

    print(f'#{test_case} {max_sum}')