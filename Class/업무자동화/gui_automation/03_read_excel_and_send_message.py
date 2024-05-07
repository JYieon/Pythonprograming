import pandas as pd
import pyautogui as pg
import pyperclip
from time import sleep

df = pd.read_excel('./message_list.xlsx')

for i, row in df.iterrows():
    # 아래 코드를 완성하여 엑셀 파일에 있는 메세지를 모두 전송하고 스크린샷을 찍어주세요.
    print(i, row['이름'])
    print(i, row['학번'])
    print(i, row['메세지'])

    pyperclip.copy(row['메세지'])
    pg.screenshot(f"{row['이름']}_{row['학번']}.png", region=(0, 0, 100, 100))

