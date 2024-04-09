# pygame 기본코드 그림불러오기, 클래스 생성, 그림변화
import pygame
# 1. 게임 초기화
pygame.init()
# 2. 게임창 옵션 설정
size = (500, 1000)
screen = pygame.display.set_mode(size)
title = "새똥 피하기"
pygame.display.set_caption(title)
# 3. 게임 내 필요한 설정
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)
def img_read(file_name, resize): 
    img = pygame.image.load(file_name+".png") #내가 입력한 경로의 그림 불러오기
    img_size = img.get_size() #그림의 사이즈 불러오기
    img_size = (img_size[0]*resize, img_size[1]*resize) #새로운 이미지 사이즈 만들기
    img = pygame.transform.smoothscale(img,img_size) #이미지 사이즈 바꾸기
    return img
person_static = img_read("man_static",0.15) #0.15배 만큼 그림 축소
person_size = person_static.get_size()
#그림파일 여러개 한번에 불러오기(달리는 순서대로)
p_list = [img_read("man_0",0.15),img_read("man_1",0.15),img_read("man_2",0.15),
          img_read("man_3",0.15),img_read("man_2",0.15),img_read("man_1",0.15)]
class person: 
    def __init__(self):
        self.img = person_static #서있는 그림으로 자기자신 초기화
        self.size = self.img.get_size()
        self.pos = tup_r((size[0]/2-self.size[0]/2,size[1]-self.size[1])) #person클래스의 위치 결정
    def show(self): #사람그림을 스크린에 그려줌
        screen.blit(self.img, self.pos)
        
player = person()
k = 0
exit = False
# 4. 메인 이벤트
while not exit:
    # 4-1. FPS 설정
    clock.tick(60) #화면 업데이트를 몇초마다 할 것인가 (화면 프레임 설정)
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    # 4-3. 입력, 시간에 따른 변화
    k += 0.2 #k값이 계속 변하면서 가져오는 그림이 달라짐-> 사람이 움직임
    kk = int(k) % 6 # 6 = len(p_list[kk])이다.
    player.img = p_list[kk]
    # 4-4. 그리기
    screen.fill(white)
    player.show()
    # 4-5. 업데이트(화면에 반영)
    pygame.display.flip()
# 5. 게임 종료
pygame.quit()