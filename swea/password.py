for test_case in range(1, 11):
    N, number = input().split()
    number = list(map(int, number))

    stack = []
    for n in number:
        if stack and stack[-1] == n:
            stack.pop()
        else:
            stack.append(n)

    print(f"#{test_case} {''.join(map(str, stack))}")
