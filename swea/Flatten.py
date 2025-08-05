for test_case in range(1, 11):
    N = int(input())
    box_lst = list(map(int, input().split()))
    for i in range(N):
        max_box = max(box_lst)
        min_box = min(box_lst)
        if max_box - min_box == 0 or max_box - min_box == 1:
            break
        box_lst[box_lst.index(max_box)] -= 1
        box_lst[box_lst.index(min_box)] += 1
    print(f'#{test_case} {max(box_lst) - min(box_lst)}')