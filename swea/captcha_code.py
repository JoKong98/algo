T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def is_captcha_code(lst):
    code = []
    result = 0
    i = 0
    while i != len(lst[1]) and lst[0]:
        value = lst[0].pop(0)
        if value == lst[1][i]:
            code.append(value)
            i += 1
        else: continue
    if code == lst[1]:
        result = 1
    return result



for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    sp_list = [[*map(int, input().split())] for _ in range(2)]
    print(f'#{test_case} {is_captcha_code(sp_list)}')