N = 4
visited = [0] * N

# 시작: 0번째 행 / 누적값: 행번호
# 종료조건: 모든 행을 고려했을 때
def recur(row):
    if row == N:
        return

    # N 개의 행을 모두 체크
    for i in range(N):
        # 이미 방문한 행이라면, 다음 행을 체크
        if visited[i]:
            continue

        # 현재 i번 째 열을 선택
        visited[i] = 1
        # 다음 재귀 호출 코드 (다음 행을 봐라)
        recur(row + 1)
        # 되돌아 왔을 때, 계산한 값을 초기화
        visited[i] = 0


recur(0)