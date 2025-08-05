T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    number_list = list(map(int,input().split()))
    max_index =len(number_list)-1 - number_list[::-1].index(max(number_list))
    min_index =number_list.index(min(number_list))
    print(f'#{test_case} {abs(max_index - min_index)}')