# 패키지 설치 필요: pip install pyautogui, pyperclip

import pyautogui
import pyautogui as pg
import pyperclip
from time import sleep

print(pg.KEYBOARD_KEYS)
# # X, Y = pyautogui.position()



# # 마우스 현재 위치 출력
# x, y = pg.position()
# print(x, y)

# # 마우스 이동
# # - 절대좌표: 화면 전체에서의 좌표
# # pyautogui.moveTo(x, y)
# # - 상대좌표: 현재 커서 위치에서의 좌표
# # pyautogui.moveRel(x, y)
# pg.moveTo(1645, 664) #원하는 좌표로 마우스 이동

# # 마우스 클릭
# # - 왼쪽 클릭
# # pyautogui.click()
# # - 오른쪽 클릭
# # pyautogui.rightClick()
# # - 왼쪽 더블 클릭
# # pyautogui.doubleClick()
# # 마우스 이동 후 클릭 후 키보드 입력
# pg.moveTo(315, 422)
# sleep(0.5)
# pg.click()
# sleep(0.5)
# pg.typewrite('1q2w3e4rq', interval=0.1)

# #로그인 버튼
# pg.moveTo(1734, 748)
# pg.click()


# # 복사 및 붙여넣기
# pyperclip.copy('안녕하세요.. 저는 홍길동입니다..') #문자열을 복사해서 클립보드에 갖고있겠다
# pg.hotkey('ctrl', 'v')

# # 엔터키 입력
# pg.hotkey('enter')