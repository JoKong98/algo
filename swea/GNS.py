T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
number_dict = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2,
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9
}
for test_case in range(1, T + 1):
    print(f'#{test_case}', end=' ')
    _,n = input().split()
    n = int(n)
    number_list = input().split()

    result = sorted(number_list,key=lambda x: number_dict[x],reverse=False)

    print(f'#{test_case}')
    print(*result)
