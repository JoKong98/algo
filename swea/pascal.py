T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

def pascal(n):
    if n == 0:
        return [1]
    prev = pascal(n-1)
    p_list = []
    p_list.append(1)
    for i in range(len(prev)-1):
        p_list.append(prev[i]+prev[i+1])
    p_list.append(1)
    return p_list

for test_case in range(1, T + 1):
    n = int(input())
    print(f'#{test_case}')
    for k in range(n):
        print(*pascal(k))

