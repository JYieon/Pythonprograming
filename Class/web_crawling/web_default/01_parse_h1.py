from bs4 import BeautifulSoup

#분석하고자 하는 html구조와 옵션을 넘겨줌
bsobj = BeautifulSoup("<html><body><h1>안녕하세요</h1><body></html>", "html.parser")
print(bsobj)

# .find() .find_all()
h1 = bsobj.find("h1") #h1부분을 찾아줌
print(h1)
print(h1.text)

