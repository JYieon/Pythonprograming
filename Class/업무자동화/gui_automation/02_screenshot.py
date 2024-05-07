import pyautogui as pg

# 스크린샷 찍기
# region = (x, y, width, height)
pg.screenshot("hello.png", region=(0, 0, 100, 100))