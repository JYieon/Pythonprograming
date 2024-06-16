import pygame
from bs4 import BeautifulSoup
import requests
import re
import random
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 600
size = [WIDTH, HEIGHT]
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("영어 끝말잇기 게임")

# 색깔 정의
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
skyblue = (100, 100, 255)

# 폰트 설정
nomal_font = pygame.font.Font(None, 50)
title_font = pygame.font.SysFont('hancomuljucheonjeonripetroglyph', 80)
guide_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 20)
finish_font = pygame.font.Font("C:/Windows/Fonts/Arial.ttf", 80)
word_font = pygame.font.Font(None, 60)

# 게임 변수
best_score = 0
use_word = []




words = []
for category in (1,19):
    url = f"https://www.englishspeak.com/ko/english-words?category_key={category}"
    res = requests.get(url)
    bsobj = BeautifulSoup(res.text, "html.parser")

    wordlist = bsobj.find("table", {"class":"table table-striped"})
    word = wordlist.find_all("a")
    
    if wordlist:
        word_links = wordlist.find_all("a")
        for link in word_links:
            word_text = link.text.strip()
            if not re.match(r'^\d', word_text) and '?' not in word_text: 
                words.append(word_text)
        

def tup_r(tup): #소수값이 안생기도록 반올림해주는 함수(정수값으로 만들어줌)
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list) #list를 tuple 형식으로 return

def find(voca):
    options = Options()
    options.add_argument('--headless')

    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)

    url = 'https://en.dict.naver.com/#/main'
    driver.get(url)
    driver.implicitly_wait(10)
    #xpath = '//input[@id="ac_input"]'
    driver.find_element(By.XPATH, '//*[@id="ac_input"]').send_keys(voca+'\n')
    driver.implicitly_wait(10)
    xpath3 = '//*[@id="searchPage_entry"]/div/div[1]/div[1]/a/strong'
    try:
        temp_voca = driver.find_element(By.XPATH, xpath3).text
        if voca != temp_voca:
            return False
        else : return True
    except Exception:
        return False
    
def use(voca, list):
    if len(list) == 0:
        return True
    elif voca in list:
        return False
    else:
        return True

# 게임 루프
exit = False
while not exit:
    current_word = random.choice(words)
    text = ''
    ready = False
    run_w = False
    game_over = False
    play_again = False
    use_word = []
    use_com = [current_word]
    enter_go = False
    player_score = 0
    win = False


    #시작화면
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #게임 종료 버튼 클릭or커멘드창에서 Ctrl+C를 입력했을 때
                exit = True   # 화면 종료
            if event.type == pygame.KEYDOWN: #키보드를 누른 후 뗄 때
                ready = True  #준비완료 -> 게임화면으로 넘어감
        if ready == True: break


        screen.fill(white)
        title = title_font.render("끝말잇기", True, skyblue)
        title_size = title.get_size()
        title_pos = tup_r((size[0]/2-title_size[0]/2, size[1]/3-title_size[1]/2)) #(46, 410)
        screen.blit(title, title_pos)

        guide = guide_font.render("PRESS ANY KEY TO START THE GAME", True, skyblue) #안내문자 하얀색 설정
        guide_size = guide.get_size()
        guide_pos = tup_r((size[0]/2-guide_size[0]/2, size[1]*4/5-guide_size[1]/2)) #(68, 709)
        if pygame.time.get_ticks() % 1000 > 500 :  #1초 주기로 안내문 깜빡거리면서 출력하도록 함
            screen.blit(guide, guide_pos)
            
        pygame.display.flip()
    
    while not exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            if event.type == pygame.KEYDOWN:
                if game_over == True: play_again = True

                key_name = pygame.key.name(event.key)
                if event.key == pygame.K_RETURN:
                    if text != "":
                        enter_go = True
                        
                elif len(key_name) == 1:
                    if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                        text = text + key_name
                    else : text = "" 
                    
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]

        screen.fill(white)
        if play_again == True : break

        if enter_go == True:
            ans = text
            if current_word[-1] != ans[0] or len(ans) < 2 or use(ans, use_word) == False: 
                game_over = True
            else:
                if find(ans) == False:
                    game_over = True

                else:
                    player_score += 1
                    use_word.append(ans)
                    if player_score > best_score : best_score = player_score
                next_words = [word for word in words if word.startswith(ans[-1])]
                if next_words:
                    current_word = random.choice(next_words)
                    if use(current_word, use_com) == True:
                        use_com.append(current_word)
                        enter_go = False
                        text = ''
                    else :
                        game_over = True
                        win = True
                else:
                    game_over = True
                    win = True
                    
        
        # 단어 표시
        comword = word_font.render(current_word, True, black)
        comword_size = comword.get_size()
        comword_pos = tup_r((size[0]*2/6-comword_size[0]/1, size[1]/3-comword_size[1]/3))
        screen.blit(comword, comword_pos)

        if text:
            userword = word_font.render(text, True, blue)
            userword_size = userword.get_size()
            userword_pos = tup_r((size[0]*3/4-userword_size[0]*2/4, size[1]/3-userword_size[1]/3))
            screen.blit(userword, userword_pos)


            
        # 입력 상자
        box_input = nomal_font.render(text, True, skyblue)
        input_size = box_input.get_size()
        input_pos = tup_r((size[0]/2-input_size[0]/2, size[1]*4/7-input_size[1]/2))
        pygame.draw.rect(screen, skyblue, (250, 315, 300, 60), 2)
        screen.blit(box_input, input_pos)
            
        # 점수 표시
        score_surface = nomal_font.render(f"Score: {player_score}", True, black)
        screen.blit(score_surface, (10, 10))
            
        #종료 화면
        if game_over == True:
            finish_bg = pygame.Surface(size) #500*900 크기의 finish_bg라는 빈 시트 생성
            finish_bg.fill(black) #검정색으로 설정
            finish_bg.set_alpha(200) #투명도 조절
            screen.blit(finish_bg, (0,0)) #화면에 출력
            if win == False :
                finish_text = "YOU LOSE" #게임 실패 멘트
            else : 
                finish_text = "YOU WIN"
            finish = finish_font.render(finish_text, True, red)
            finish_size = finish.get_size() #성공시 (246,34) 실패시 (257,34)
            finish_pos = tup_r((size[0]/2-finish_size[0]/2, size[1]/3-finish_size[1]/3))
            screen.blit(finish, finish_pos) #finish화면 출력
            score = nomal_font.render(f"Best Score : {best_score}", True, white)
            score_size = score.get_size()
            score_pos = tup_r((size[0]/2-score_size[0]/2, size[1]*3/5-score_size[1]/2))
            screen.blit(score, score_pos)
            guide = guide_font.render("PRESS ANY KEY TO PLAY AGAIN", True, white) #재시작 안내문
            guide_size = guide.get_size() #(309, 23)
            guide_pos = tup_r((size[0]/2-guide_size[0]/2, size[1]*4/5-guide_size[1]/2)) #(96, 270)
            screen.blit(guide, guide_pos) #안내문 화면에 출력

        pygame.display.flip()

pygame.quit()
