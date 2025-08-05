T = int(input())
 # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    li = list(map(int,input().split()))
    count = 0
    for i in range(2,N-1):
        if i == 2:
            if li[i] >= li[i+1] and li[i] >= li[i+2]:
                if li[i+1]>=li[i+2]:
                    count += li[i]-li[i+1]

                else:
                    count += li[i]-li[i+2]

        elif i == N-2:
            if li[i] >= li[i-1]and li[i] >= li[i-2]:
                if li[i-1]>=li[i-2]:
                    count += li[i]-li[i-1]

                else:
                    count += li[i]-li[i-2]

        else:
            if li[i]>=li[i-1] and li[i]>=li[i+1] and li[i]>=li[i-2] and li[i]>=li[i+2]:
                li_compare = [li[i - 2], li[i - 1], li[i + 1] , li[i + 2]]
                count += li[i] -sorted(li_compare)[3]

            else:
                continue



    print(f'#{test_case} {count}')




    # ///////////////////////////////////////////////////////////////////////////////////