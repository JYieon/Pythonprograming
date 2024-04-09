#키보드 입력을 통한 이동 구현 추가
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
    img = pygame.image.load(file_name+".png")
    img_size = img.get_size()
    img_size = (img_size[0]*resize, img_size[1]*resize)
    img = pygame.transform.smoothscale(img,img_size)
    return img
person_static = img_read("char_static",0.15) #사람 그림 변경됨
person_size = person_static.get_size()
p_list = [img_read("char_0",0.15),img_read("char_1",0.15),img_read("char_2",0.15),
          img_read("char_3",0.15)]
class person:
    def __init__(self):
        self.img = person_static
        self.size = self.img.get_size()
        self.pos = tup_r((size[0]/2-self.size[0]/2,size[1]-self.size[1]))
        self.move = 10
    def show(self):
        screen.blit(self.img, self.pos)
        
player = person()
k = 0
left_go = False #왼쪽으로 가기
right_go = False #오른쪽으로 가기
exit = False
# 4. 메인 이벤트
while not exit:
    # 4-1. FPS 설정
    clock.tick(60)
    # 4-2. 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN: #키를 누른 경우
            key_name = pygame.key.name(event.key) #무슨 키인지 이름 확인
            if key_name == "left":
                left_go = True
            elif key_name == "right":
                right_go = True
        if event.type == pygame.KEYUP: #키를 눌렀다가 떼는 순간
            key_name = pygame.key.name(event.key)
            if key_name == "left":
                left_go = False
            elif key_name == "right":
                right_go = False
    # 4-3. 입력, 시간에 따른 변화
    #k += 0.2
    #k = int(k) % len(p_list)
    #layer.img = p_list[kk]
    if left_go == True and right_go == False:
        player.pos = (player.pos[0]-player.move, player.pos[1]) #player.move값으로 속도조절
        if player.pos[0] <= 0: #화면 밖으로 나가지 않도록 조정
            player.pos = (0, player.pos[1])
    elif left_go == False and right_go == True:
        player.pos = (player.pos[0]+player.move, player.pos[1])
        if player.pos[0] >= size[0]-player.size[0]:
            player.pos = (size[0]-player.size[0], player.pos[1])        
    # 4-4. 그리기
    screen.fill(white)
    player.show()
    # 4-5. 업데이트
    pygame.display.flip()
# 5. 게임 종료
pygame.quit()