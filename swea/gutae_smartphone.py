T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    cordinate = [[*map(int, input().split())] for _ in range(2)]
    if cordinate[0][2] > cordinate[1][2] and cordinate[0][3] > cordinate[1][3]:
        cordinate[0], cordinate[1] = cordinate[1], cordinate[0]
    x1,y1,x2,y2 = map(int,cordinate[0])
    x3,y3,x4,y4 = map(int, cordinate[1])
    if x3<=x2 and y3<=y2:
        result = 1
    elif (x3-x2 == 1 and y3>= y1 and y3<=y2) or (y3 - y2 ==1 and x3>=x1 and x3<=x2):
        result = 2
    elif (x3 - x2 ==1 and y3 - y2 ==1):
        result = 3
    else:
        result = 4
    print(f'#{test_case} {result}')


            
            
    # print(f'{test_case} {result}')
    
     
    # if [dat[i][j] for i in range(cordinate[1][1], cordinate[1][3]+1) for j in range(cordinate[1][0], cordinate[1][2]+1) if dat[i][j] ==1]:
    #     result = 1    # 겹치지는 않지만 2의 시작점 x, y좌표가 1의 끝점 x, y보다 x가 작고 y의 차이가 1인 경우 혹은 -1인경우 혹은 y가 작고 x의 차이가 1이거나 -1인경우
    # elif [dat[i][j] for i in (cordinate[0][1]-1,cordinate[0][3]+1) for j in range(cordinate[0][0]+1,cordinate[0][2]) if dat[i][j] == 1]:
    #     result = 2
    # elif [dat[i][j] for j in (cordinate[0][0]-1, cordinate[0][3]+1) for i in range(cordinate[0][1]+1, cordinate[0][3]) if dat[i][j] ==1]:
    #     result = 2
    # elif [dat[i][j] for i, j in ((cordinate[0][1]-1,cordinate[0][0]-1), (cordinate[0][1]-1,cordinate[0][2]+1), (cordinate[0][3]+1,cordinate[0][0]-1), (cordinate[0][3]+1,cordinate[0][2]+1)) if dat[i][j] == 1]:
    #     result = 3
    # else:
    #     result = 4
            
            
            
            
    # print(f'{test_case} {result}')