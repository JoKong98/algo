T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    M_number = list(map(int, input().split()))
    fu_charge = K
    charge_count = 0
    for i in range(1,N):
        fu_charge -= 1
        if fu_charge == 0:
            if i in M_number:
                fu_charge = K
                charge_count += 1
            else:
                charge_count = 0
                break
        else:
            if i + fu_charge < N:
                if i + fu_charge not in M_number:
                    if i in M_number:
                        fu_charge = K
                        charge_count += 1

    print(f'#{test_case} {charge_count}')