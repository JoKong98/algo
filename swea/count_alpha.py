T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    dat = [0] * 26
    word = input()
    for i in range(len(word)):
        dat[ord(word[i])-97] += 1
    print(f"#{test_case}", end=' ')
    print(*dat)


