for test_case in range(1,11):
    n = int(input())
    pld_arr = [list(input().strip()) for _ in range(100)]
    k = 0
    max_len = 0
    for i in range(100):
        for j in range(100):
            for k in range(101):
                if j+k<=100:
                    word = pld_arr[i][j:j+k]
                    if len(word) != 0:
                        if word == word[::-1]:
                            if max_len< len(word):
                                max_len = len(word)
                        else: continue
                    else: continue
                else: continue
    k = 0
    pld_arr= list(zip(*pld_arr))

    for i in range(100):
        for j in range(100):
            for k in range(101):
                if j+k<=100:
                    word = pld_arr[i][j:j+k]
                    if len(word) != 0:
                        if word == word[::-1]:
                            if max_len< len(word):
                                max_len = len(word)
                        else: continue
                    else: continue
                else: continue
    print(f'#{n} {max_len}')