import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.naver?code=005930"
res = requests.get(url)
bsobj = BeautifulSoup(res.text, "html.parser")
print(bsobj)
div_today = bsobj.find("div", {"class":"today"})
print(div_today)
em = div_today.find("em")
print(em)
price = em.find("span", {"class":"blind"}).text
print(price)




