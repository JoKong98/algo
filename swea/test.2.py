T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    a, b = map(int,input().split())
    numbers = list(map(int, input().split())
    ne_numbers = []
    for i in range(b):
        max_hap = 0
        for j in range(b):
            max_hap += numbers[i+j]
        ne_numbers.append(max_hap)
    print(f'#{test_case} {max(ne_numbers)-min(ne_numbers)}')