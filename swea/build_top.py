import sys
sys.stdin = open("input.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M2, M1 = map(int,input().split())
    block = [*map(int, input().split())]
    block = sorted(block)
    t1 = []
    t2 = []
    k = 1
    v = block.pop()
    if M1 > M2:
        t1.append(v * k)
    else:
        t2.append(v * k)
    while block:
        v = block.pop()
        if len(t1) > len(t2):
            if len(t2)!=M2:
                t2.append(v *(k+len(t2)))
            else:
                t1.append(v * (k + len(t1)))
                while block:
                    t1.append(block.pop()*(k+len(t1)))
        else:
            if len(t1) != M1:
                t1.append(v *(k+len(t1)))
            else:
                t2.append(v * (k + len(t2)))
                while block:
                    t2.append(block.pop()*(k+len(t2)))
    print(f'#{test_case} {sum(t1)+sum(t2)}')



