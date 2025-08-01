
# 내가 처음 짠 것 
# matrix = [list(map(int,input().split())) for _ in range(4)]
# empty_space = [[0]* 100 for _ in range(100)]
# for i in range(4):
#     for j in range(matrix[i][0],matrix[i][2]):
#         for k in range(matrix[i][1],matrix[i][3]):
#             empty_space[99-j][k] = 1
# count = 0
# for i in range(100):
#     for j in range(100):
#         if empty_space[i][j] == 1:
#             count += 1
#         else:
#             continue
        
# print(count)
# 개선안
# 개선 포인트. 이중 포문 만을 이용해 리스트 컴프리헨션으로 깔끔하게 정리, set을 이용해 자동으로 중복 제거 처리, l에 리스트 안에 튜플 형식으로 저장해서 중복 제거 처리
B=[[int(x)for x in input().split()]for _ in range(4)]
L = set()
for x1,y1,x2,y2 in B:
    l = [(dx,dy)for dx in range(x1,x2)for dy in range(y1,y2)]
    L.update(l)
print(len(L))