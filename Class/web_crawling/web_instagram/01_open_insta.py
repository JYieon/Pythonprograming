from selenium import webdriver
import chromedriver_autoinstaller
import time

chromedriver_autoinstaller.install() #크롬에서 진행하겠다.

driver = webdriver.Chrome()
driver.implicitly_wait(3) #3초 정도 기다리는 것.

url = "https://www.instagram.com/" #탐색하고자 하는 url
driver.get(url=url)
time.sleep(20) #실행된 화면이 20초후 자동으로 꺼짐
xpath = '//*[@id="loginForm"]/div/div[1]/div/label/input'