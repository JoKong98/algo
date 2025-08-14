for test_case in range(1,11):
    t, n = map(int, input().split())
    l = [[] for _ in range(101)]
    d = [*map(int, input().split())]
    for k, v in zip(d[::2], d[1::2]):
        l[k].append(v)
    visited = set()


    def rd(n, destination = 99):
        visited.add(n)
        if destination in visited:
            return
        if n == destination:
            return
        for i in l[n]:
            if i not in visited:
                rd(i)
            else:
                visited.add(i)
                break

    rd(0)
    if 99 in visited:
        result = 1
    else:
        result = 0

    print(f"#{test_case} {result}")









