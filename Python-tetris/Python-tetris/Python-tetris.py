import random
import array

class System:
    #공간 생성
    x = 0
    y = 0
    grid = array(b,)
    while x <= 10:
        while y <= 20:
            grid = [[0 for col in range(11)] for row in range(10)]
            y += 1
        x += 1
    #점수 선언
    score = 0
    #라인클리어 체크 함수
    def clearLine():
        checkClear = 1
        combo = 0
        while checkClear == 1:
            checkClear = 0
            y = 1
            combo += 1
            while y <= 20:
                x = 0
                #한 y축에서 모든 x가 채워졌는지 확인
                while x <= 10:
                    #빈 공간이 있을 경우 반복문 해제
                    if grid[x,y] == 0:
                        break
                    x += 1
                    #모든 공간이 채워졌을 경우 라인 클리어
                    if _x == 10 and grid[x, y] == 1:
                        x = 0
                        checkClear = 1
                        #라인 클리어
                        while x <= 10:
                            grid[x, y] = 0
                            x += 1
                            score += 100*combo
                        #위에 있는 모든 블럭 한 칸 아래로 당기기
                        while y > 0:
                            x = 0
                            while _x <= 10:
                                grid[x, y] = grid[x, y-1]
                                x += 1
                            y -= 1
    def CreateBlock():
        #블럭 형태 결정
        blockType = random.choice("Z,T,O,L");
        if blockType == "Z":
            grid[5,0] = 2

sysObj = System()
sysObj.clearLine()
print(sysObj.score)

print("배열이 c++이랑 좀 많이 다름")