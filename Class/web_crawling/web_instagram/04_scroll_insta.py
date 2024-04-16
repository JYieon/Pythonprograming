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

id = os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")

input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
input_id.send_keys(id)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
# driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)

time.sleep(5)

url = f"https://www.instagram.com/explore/"
driver.get(url=url)
time.sleep(6)
# print(driver.page_source)

for _ in range(20):
    #윈도우 창을 어디까지 스크롤해라
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5) #5초 쉬면서 반복
    



