for test_case in range(1):
    ladder = [[*map(int, input().split())] for _ in range(100)]
    dx = [-1, 1]
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 2:
                start_x, start_y = j, i
    while start_y != 0:
        # 왼쪽 확인
        # 오른쪽 확인

        for x in dx:
            nj = start_x + x
            if start_y <0 or nj >= 100 or nj < 0:
                continue
            else:
                while ladder[start_y][nj] != 0:
                    start_x = nj
                    nj = start_x + x
                break
        start_y -= 1

    print(start_x)


