T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = [[*map(int, input().split())] for _ in range(9)]
    result = 1
    for i in range(9):
        check = [arr[i][j] for j in range(9)]
        check.set()
        if len(check) != 9:
            result = 0
    for j in range(9):
        check = [arr[i][j] for i in range(9)]
        check.set()
        if len(check) != 9:
            result = 0
    for i in range(0,9,3):
        check = [arr[i][j] for j in range(0,3)]
        if len(check) != 9:
            result = 0
    print(f'#{test_case} {result}')
