def len_of_one(word):
    res = 0
    for _ in word:
        res += 1
    return res


for t in range(int(input())):
    _ = input()
    print(f'#{t + 1} {max(map(len_of_one, input().split("0")))}')