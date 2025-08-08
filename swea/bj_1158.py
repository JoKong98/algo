n, k = map(int, input().split())
people = [i for i in range(1, n+1)]
x = 0
result = []
while len(people) != 0:
    z = 0
    while z < k-1:
        if x> len(people)-1:
            x = 0
        else:
            z+=1
            x += 1
    if x > len(people)-1:
        x = 0
    result.append(people.pop(x))



print(f"<{', '.join(map(str,result))}>")