#hangman 주석쓰기 과제
import pygame, math, random

# 1. 게임 초기화
pygame.init()

# 2. 게임창 옵션 설정
size = [500,900]
screen = pygame.display.set_mode(size) #게임 스크린 창을 500X900 사이즈로 설정
pygame.display.set_caption("HANGMAN") #게임 상단바에 "HANGMAN" 출력

# 3. 게임 내 필요한 설정 
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
hint_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 80)
entry_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 60)
no_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 40)
title_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 80)
guide_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
finish_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 30)
sound_bad = pygame.mixer.Sound("bad.ogg")
sound_good = pygame.mixer.Sound("good.ogg")
sound_clock = pygame.mixer.Sound("clock.ogg")
sound_save = pygame.mixer.Sound("save.ogg")
sound_fail = pygame.mixer.Sound("fail.ogg")
sound_bad.set_volume(0.2)
sound_good.set_volume(0.2)
sound_clock.set_volume(0.2)
sound_save.set_volume(0.2)
sound_fail.set_volume(0.2)

def tup_r(tup): #소수값이 안생기도록 반올림해주는 함수(정수값으로 만들어줌)
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list) #list를 tuple 형식으로 return
exit = False
while not exit:
    entry_text = ""
    drop = False
    enter_go = False
    ready = False
    game_over = False
    save = False
    play_again = False

    #  A가 영어 단어를 1개 생각한다.
    f = open("voca.txt","r",encoding='UTF-8')  
    raw_data = f.read() #vaca.txt를 읽어서 raw_data에 저장한다.
    f.close()
    data_list = raw_data.split("\n")  #raw_data에서 줄바뀜을 기준으로 단어를 나눠서 data_list에 저장한다.
    data_list = data_list[:-1] #리스트의 마지막 데이터를 제외한 전체 데이터 저장(마지막데이터는 공백임)
    while True:
        r_index = random.randrange(0,len(data_list)) # 0~data_list의 길이만큼의 숫자 하나 선택
        #r_index 위치에 저장된 단어의 '\xa0'를 공백으로 바꾸고 공백을 기준으로 잘라서 저장, 1번위치에 있는 영어단어를 word에 저장
        word = data_list[r_index].replace(u"\xa0", u" ").split(" ")[1] 
        if len(word) <= 6 :break #word의 길이가 6이 넘지 않도록 한다.
    word = word.upper() #word 단어를 대문자로 바꾼다.
    
    #  단어의 글자 수만큼 밑줄을 긋는다.
    word_show = "_"*len(word)
    try_num = 0 #시도 횟수
    ok_list = [] #맞춘 알파벳 저장하는 list
    no_list = [] #틀린 알파벳 저장하는 list

    k = 0
    # 시작 화면
    sound_save.stop()
    sound_fail.stop()
    while not exit:
        clock.tick(60) #초당 60번의 화면을 띄어준다(초당 60프레임)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #게임 종료 버튼 클릭or커멘드창에서 Ctrl+C를 입력했을 때
                exit = True   # 화면 종료
            if event.type == pygame.KEYDOWN: #키보드를 누른 후 뗄 때
                ready = True  #준비완료 -> 게임화면으로 넘어감
        if ready == True: break             
        
        screen.fill(black) #스크린 색상은 검은색으로 설정
        title = title_font.render("HANGMAN", True, white)  #타이틀 폰트는 하얀색 설정
        title_size = title.get_size() #(409,90) 
        title_pos = tup_r((size[0]/2-title_size[0]/2, size[1]/2-title_size[1]/2)) #(46, 410)
        screen.blit(title, title_pos) #title 화면에 출력

        guide = guide_font.render("PRESS ANY KEY TO START THE GAME", True, white) #안내문자 하얀색 설정
        guide_size = guide.get_size() #(365, 23)
        guide_pos = tup_r((size[0]/2-guide_size[0]/2, size[1]*4/5-guide_size[1]/2)) #(68, 709)
        if pygame.time.get_ticks() % 1000 > 500 :  #1초 주기로 안내문 깜빡거리면서 출력하도록 함
            screen.blit(guide, guide_pos) #안내문 화면에 출력

        pygame.display.flip() #화면에 출력
        
    # 4. 메인 이벤트
    sound_clock.play(-1) #clock.ogg 무한반복
    while not exit:
        # 4-1. FPS 설정
        clock.tick(60) #초당60프레임
        # 4-2. 각종 입력 감지
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #게임 종료 버튼 클릭or커멘드창에서 Ctrl+C를 입력했을 때
                exit = True # 화면 종료
            if event.type == pygame.KEYDOWN: #키가 눌렸을 때
                if drop == False and try_num == 8: 
                    continue 
                if game_over == True: play_again = True 
                key_name = pygame.key.name(event.key) #사용자가 입력한 키보드의 key를 key_name에 저장

                if (key_name == "return" or key_name == "enter"): #사용자가 return키나 enter키를 눌렀을 때
                    if entry_text != "" and (ok_list+no_list).count(entry_text) == 0 : #입력한 알파벳이 처음 입력됐을 때
                        enter_go = True            

                elif len(key_name) == 1: #사용자가 key_name이 1인 key를 눌렀을 때
                    #ord함수 : 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수 반환
                    #입력된 키가 알파벳 대문자 or 소문자 일 때
                    if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                        entry_text = key_name.upper() #입력받은 알파벳 대문자로 바꿔서 entry_text에 저장
                    else : entry_text = "" #입력된 키가 알파벳이 아니면 entry_text에 아무것도 저장 안함

                else : entry_text = ""

        # 4-3. 입력, 시간에 따른 변화
        if play_again == True : break
        if try_num == 8 : k += 1 # 시도 횟수가 8이면 k값 증가

        if enter_go == True:
            ans = entry_text #입력받은 알파벳 ans에 저장
            result = word.find(ans) #맞춰야 하는 word에 ans가 있는지 찾기
            if result == -1 : #없음
                try_num += 1 #시도 횟수 증가
                no_list.append(ans) #word에 없는 알파벳은 no_list에 저장
                sound_bad.play()
            else : #있음
                ok_list.append(ans) #word에 있는 알파벳은 ok_list에 저장
                for i in range(len(word)):
                    if word[i] == ans: #word i번 인덱스에 ans가 있다면 
                        word_show = word_show[:i] + ans + word_show[i+1:] #word_show의 i번째 index에 ans 삽입
                sound_good.play()
            enter_go = False
            entry_text = "" #입력창을 다시 비워둔다.

        if drop == True: # 실패로 종료
            game_over = True
            word_show = word
            sound_clock.stop()
            
        if word_show.find("_") == -1 and game_over == False : # 성공으로 종료
            game_over = True
            save = True
            sound_clock.stop()
            sound_save.play()

        # 4-4. 그리기
        screen.fill(black) #스크린 화면은 블랙
        A = tup_r((0, size[1]*2/3)) #(0, 600)
        B = (size[0], A[1]) #(500, 600)
        C = tup_r((size[0]/6 , A[1])) #(83, 600)
        D = (C[0], C[0]) #(83, 83)
        E = tup_r((size[0]/2, D[1])) #(250, 83)
        if save != True:
            #hangman시작할 때 나오는 기본 선들이 그려짐
            pygame.draw.line(screen, white, A, B, 3) #하얀 선을 3의 굵기로 A부터 B지점까지 그림
            pygame.draw.line(screen, white, C, D, 3) #하얀 선을 3의 굵기로 C부터 D지점까지 그림
            pygame.draw.line(screen, white, D, E, 3) #하얀 선을 3의 굵기로 D부터 E지점까지 그림
        F = tup_r((E[0], E[1]+size[0]/6)) #(250, 166)
        if drop == False and save != True:
            pygame.draw.line(screen, white, E, F, 3)  #하얀 선을 3의 굵기로 E부터 F지점까지 그림
        r_head = round(size[0]/12) #hangman머리 반지름 42
        if drop == True : G = (F[0],F[1]+r_head+k*10) #drop이 true가 되면 G좌표가 아래로 떨어지도록 설정
        else : G = (F[0],F[1]+r_head) #(250, 208)
        ##시도 횟수 1번 이상 or 성공으로 종료됐을 때 머리를 그린다.
        if try_num >= 1 or save == True: pygame.draw.circle(screen, white, G, r_head, 3)
        H = (G[0], G[1]+r_head) #(250, 250)
        I = (H[0], H[1]+r_head) #(250, 292)
        ##시도 횟수 2번 이상 or 성공으로 종료됐을 때 몸통1을 그린다.
        if try_num >= 2 or save == True:pygame.draw.line(screen, white, H, I, 3)
        l_arm = r_head*2 #84
        J = (I[0]-l_arm*math.cos(30*math.pi/180), 
            I[1]+l_arm*math.sin(30*math.pi/180))
        K = (I[0]+l_arm*math.cos(30*math.pi/180),
            I[1]+l_arm*math.sin(30*math.pi/180))
        J = tup_r(J) #정수로 변환 (177, 334)
        K = tup_r(K) #(323, 334)
        ##시도 횟수 3번 이상 or 성공으로 종료됐을 때 왼쪽 팔을 그린다.
        if try_num >= 3 or save == True:pygame.draw.line(screen, white, I, J, 3)
        #시도 횟수 4번 이상 or 성공으로 종료됐을 때 오른쪽 팔을 그린다.
        if try_num >= 4 or save == True:pygame.draw.line(screen, white, I, K, 3)
        L = (I[0], I[1]+l_arm) #(250, 376)
        ##시도 횟수 5번 이상 or 성공으로 종료됐을 때 몸통2를 그린다.
        if try_num >= 5 or save == True:pygame.draw.line(screen, white, I, L, 3)
        l_leg = round(l_arm * 1.5) #126
        M = (L[0]-l_leg*math.cos(60*math.pi/180), 
            L[1]+l_leg*math.sin(60*math.pi/180))
        N = (L[0]+l_leg*math.cos(60*math.pi/180),
            L[1]+l_leg*math.sin(60*math.pi/180))  
        M = tup_r(M) #(187, 485)
        N = tup_r(N) #(313, 485)
        ##시도 횟수 6번 이상 or 성공으로 종료됐을 때 왼쪽 다리를 그린다.
        if try_num >= 6 or save == True:pygame.draw.line(screen, white, L, M, 3)
        ##시도 횟수 7번 이상 or 성공으로 종료됐을 때 오른쪽 다리를 그린다.
        if try_num >= 7 or save == True:pygame.draw.line(screen, white, L, N, 3)  
        if drop == False and try_num == 8: #8번 시도했을때
            O = tup_r((size[0]/2-size[0]/6, E[1]/2+F[1]/2)) #(167, 125)
            P = (O[0]+k*2, O[1]) #(167+k*2, 126) 가로로 점점 길어짐
            if P[0] > size[0]/2+size[0]/6 : #P[0]값이 333보다 커지면
                P = tup_r((size[0]/2+size[0]/6, O[1])) # P = (333, 125)
                drop = True #hangman이 아래로 떨어짐
                k = 0 
                sound_fail.play()
            pygame.draw.line(screen, red, O, P, 3) #빨간 선으로 O부터 P까지 그려준다.

        # 힌트 표시하기
        hint = hint_font.render(word_show, True, white) 
        hint_size = hint.get_size() #(x, 90) -> x값은 단어 길이에 따라 매번 바뀜
        hint_pos = tup_r((size[0]/2-hint_size[0]/2, size[1]*5/6-hint_size[1]/2)) #(250-hint_size[0]/2, 705)
        screen.blit(hint, hint_pos) #힌트 화면에 출력

        # 입력창 표시하기
        entry = entry_font.render(entry_text, True, black) #사용자가 입력하는 text 설정
        entry_size = entry.get_size() #(0,68)
        entry_pos = tup_r((size[0]/2-entry_size[0]/2, size[1]*17/18-entry_size[1]/2)) #(216, 816)
        entry_bg_size = 80
        pygame.draw.rect(screen, white, tup_r((size[0]/2-entry_bg_size/2, size[1]*17/18-entry_bg_size/2
                                        ,entry_bg_size ,entry_bg_size))) #(tup_r(210, 810, 80, 80))=>(x축, y축, 가로, 세로)
        screen.blit(entry, entry_pos) #입력창 화면에 출력

        # 오답 표시하기
        no_text = " ".join(no_list) #no_list의 알파벳에 공백을 붙여서 no_text에 저장
        no = no_font.render(no_text, True, red) #no_text의 색깔을 red지정하여 no에 저장
        no_pos = tup_r((20, size[1]*2/3+20)) #(20, 620)
        screen.blit(no, no_pos) #오답 알파벳 화면에 출력

        # 종료 화면
        if game_over == True:
            finish_bg = pygame.Surface(size) #500*900 크기의 finish_bg라는 빈 시트 생성
            finish_bg.fill(black) #검정색으로 설정
            finish_bg.set_alpha(200) #투명도 조절
            screen.blit(finish_bg, (0,0)) #화면에 출력
            if save == True: finish_text = "You saved the man" #게임 성공 멘트
            else : finish_text = "You killed the man" #게임 실패 멘트
            finish = finish_font.render(finish_text, True, white)
            finish_size = finish.get_size() #성공시 (246,34) 실패시 (257,34)
            finish_pos = tup_r((size[0]/2-finish_size[0]/2, size[1]*3/4-finish_size[1]/2))
            screen.blit(finish, finish_pos) #finish화면 출력
            guide = guide_font.render("PRESS ANY KEY TO PLAY AGAIN", True, white) #재시작 안내문
            guide_size = guide.get_size() #(309, 23)
            guide_pos = tup_r((size[0]/2-guide_size[0]/2, size[1]*4/5-guide_size[1]/2)) #(96, 270)
            screen.blit(guide, guide_pos) #안내문 화면에 출력

        # 4-5. 업데이트
        pygame.display.flip()

# 5. 게임 종료
pygame.quit()
