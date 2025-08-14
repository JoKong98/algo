import sys
sys.stdin = open("input/calculator1_input.txt")

# 1. 중위 -> 후위 표기법으로 전환
def trans_back(tokens):
    stack = []
    oper_stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(token)
        else:
            if oper_stack:
                stack.append(oper_stack.pop())
            oper_stack.append(token)
    stack.append(oper_stack.pop())
    return stack

def calculate(tokens):
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            stack.append(num1 + num2)
    return stack[0]

for tc in range(1,11):
    n = int(input())
    row = input()
    postfix = trans_back(row)
    result = calculate(postfix)
    print(f'#{tc} {result}')