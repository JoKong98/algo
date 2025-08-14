def cola(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + cola(n // 2)
    else:
        return 1 + cola(n * 3 + 1)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print(f'#{test_case} {cola(N)}')