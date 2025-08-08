T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # arr = [[0] * 15 for i in range(5)]
    # word = [input() for i in range(5)]
    # for i in range(5): # 5개니까 5번 반복
    #     for j in range(len(word[i])): #word의 글자 수만큼 반복
    #         arr[i][j] = word[i][j] # arr에 재할당
    #
    # print(f'#{test_case}', end=' ')
    # for j in range(15):
    #     for i in range(5):
    #         if arr[i][j] == 0:
    #             continue
    #         else:
    #             print(arr[i][j], end='')
    # print()
    word = [input() for i in range(5)]
    k = 0

    print(f'#{test_case}', end=' ')
    while k<5:
        for j in range(len(word[k])):
            for i in range(5):
                print(word[i][j], end='')
            k+=1
    print()