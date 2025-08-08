T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
mirror_dict = {
    'b' : 'd',
    'd' : 'b',
    'p' : 'q',
    'q' : 'p'
}
for test_case in range(1, T + 1):
    word = input()
    print(f'#{test_case}', end= ' ')
    for i in range(len(word)-1,-1,-1):
        print(f'{mirror_dict[word[i]]}',end='')
    print()