T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number = list(map(int, input()))
    count_list = [0] * 10
    for i in number:
        count_list[i] += 1
    result = [[i,count] for i, count in enumerate(count_list)]
    sorted_list = sorted(result, key = lambda x: (x[1],x[0]), reverse=True)

    print(f'#{test_case} {sorted_list[0][0]} {sorted_list[0][1]}')