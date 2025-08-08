T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    A, B = input().split()
    count = 0
    i = 0
    while i<=len(A)-1:
        if A[i:i+len(B)] == B:
            count += 1
            i += len(B)
        else:
            count += 1
            i += 1
    print(f'#{test_case} {count}')