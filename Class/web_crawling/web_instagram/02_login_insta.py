from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(3)

url = "https://www.instagram.com/"
driver.get(url=url)

#id = "hell"
#password = "world" #보안상 매우 안좋음. 정보가 코드에 노출되면 안됨.
id = os.getenv("INSTA_ID") #환경변수 설정으로 정보 노출 막기(INSTA_ID, INSTA_PW추가)
password = os.getenv("INSTA_PW")
input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
#설정한 요소에 id입력(키보드로 하는 행위)
input_id.send_keys(id)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
#driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)

time.sleep(200)