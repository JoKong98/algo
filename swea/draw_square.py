T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input()) # 게임판의 크기
    game_arr = [[*map(int, input().split())] for _ in range(N)] # 게임판 생성
    max_area = 0
    count = 0
    max_area_list = []
    for i in range(N):
        for j in range(N):
            for k in range(N):
                for m in range(N):
                    ni = i+k
                    nj = j+m
                    if ni<N and nj<N:
                        if game_arr[i][j] == game_arr[ni][nj]:
                            area = (ni+1-i) * (nj+1-j)
                            if max_area <= area:
                                max_area = area
                                max_area_list.append(max_area)
        
    print(f'#{test_case} {max_area_list.count(max_area)}')
                        
                    
    
    