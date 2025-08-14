d = {
    '{':'}',
    '[':']',
    '(':')',
    '<':'>'
}
for test_case in range(1, 11):
    n = int(input())
    lst = input()
    cnt = []
    for i in range(n):
        if lst[i] in ['{','[','(','<']:
            cnt.append(lst[i])
        else :
            if lst[i] != d[cnt[len(cnt)-1]]:
                break
            else:
                cnt.pop()

    print(f'#{test_case} {0 if cnt else 1}')

