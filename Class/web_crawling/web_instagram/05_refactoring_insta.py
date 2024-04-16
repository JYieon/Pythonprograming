from selenium import webdriver
import chromedriver_autoinstaller
import time
import os

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

chromedriver_autoinstaller.install()

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "https://www.instagram.com/"
driver.get(url=url)


def login(id, password):
    input_id = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    input_id.send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
    # driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').send_keys(Keys.ENTER)

def search(hashtag, scroll_times):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    driver.get(url=url)
    time.sleep(3)
    # print(driver.page_source)

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

def like_comment(row, col, comment, repeat=3):
    #xpath를 알아야지 row와col에 맞는 그림을 클릭 가능
    xpath = f'/html/body/div[2]/div/div/div[2]/div/div/div[1]/section/main/article/div/div[2]/div/div[{row}]/div[{col}]/a/div[1]/div[2]'
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(6)
    for _ in range(repeat):
        # like
        like_xpath = "//*[name()='svg'][@aria-label='좋아요']"
        driver.find_element(By.XPATH, like_xpath).click()

        time.sleep(4)

        # comment
        comment_xpath = "//*[name()='textarea'][@aria-label='댓글 달기...']"
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)
        driver.find_element(By.XPATH, comment_xpath).send_keys(Keys.ENTER)

        time.sleep(4)

        # 다음 게시물 버튼 누르기(오른쪽 화살표)
        next_xpath = "//*[name()='svg'][@aria-label='다음']"
        driver.find_element(By.XPATH, next_xpath).click()

        time.sleep(4)


id = os.getenv("INSTA_ID")
password = os.getenv("INSTA_PW")
login(id, password)

time.sleep(5)

# Search
hashtag = "강아지"
search(hashtag, 0)

# like comment
like_comment(2, 3, "강아지가 귀엽네요", 2)

time.sleep(200)
