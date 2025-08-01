matrix = [list(map(int,input().split())) for _ in range(4)]
empty_space = [[0]* 100 for _ in range(100)]
for i in range(4):
    for j in range(matrix[i][0],matrix[i][2]):
        for k in range(matrix[i][1],matrix[i][3]):
            empty_space[99-j][k] = 1
count = 0
for i in range(100):
    for j in range(100):
        if empty_space[i][j] == 1:
            count += 1
        else:
            continue
        
print(count)
        
