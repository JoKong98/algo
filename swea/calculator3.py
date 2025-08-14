import sys
sys.stdin=open("input.txt")

priority = {
    '+' : 1,
    '*' : 2,
    '(' : 0
}

def trans_back(tokens):
    stack = []
    oper_stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(token)
        elif token == '(':
            oper_stack.append(token)
        elif token == ')':
            if oper_stack:
                top_oper = oper_stack.pop()
                while top_oper != '(':
                    stack.append(top_oper)
                    top_oper = oper_stack.pop()

        else:
            while oper_stack and priority[oper_stack[-1]] >= priority[token]:
                stack.append(oper_stack.pop())
            oper_stack.append(token)
    while oper_stack:
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
            if priority[token] == 1:
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)

    return stack[0]
for tc in range(1,11):
    n = int(input())
    row = input()
    postfix = trans_back(row)
    result = calculate(postfix)
    print(f'#{tc} {result}')