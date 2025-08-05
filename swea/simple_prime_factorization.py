T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    number = int(input())
    N =[2,3,5,7,11]
    li = [0] * 5
    for i in range(5):
        while number % N[4-i] == 0:
            li[4 - i] += 1
            number /= N[4 - i]
        if number // 2 == 0:
            break

    print(f'#{test_case}', end = ' ')
    for i in range(5):
        print(f'{li[i]}', end = ' ')
    print()