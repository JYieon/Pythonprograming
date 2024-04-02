import random

#word = "mana"

f = open("../Class/hangman/voca.txt", "r", encoding='UTF-8')
raw_data = f.read()
f.close
#print(raw_data)

data_list = raw_data.split("\n")
#print(data_list) #list는 배열이고 마지막 원소가 비어있음.

print(data_list[:-1])

while True:
    random_idx = random.randrange(0, len(data_list))
    word = data_list[random_idx].replace(u"\xa0", u" ").split(" ")[1] #\xa0을 띄어쓰기로 바꾸고 공백으로 나눠진 문장에서 1번에 있는 단어 저장(0번->1번)
    if len(word) <= 6:
        break
#quit() #즉시 프로그램 종료 (밑의 코드 실행 안함)



word = word.upper()
print(word)
word_show = "_"*len(word)
print(word_show)


try_num = 0
ok_list = []
no_list = []
while True: #보통 게임은  while문으로 시작
    ans = input().upper()
    print(ans)

    result = word.find(ans) #입력한 글자 찾기 있으면1, 없으면 -1 return
    if result == -1:
        print("없음")
        try_num += 1
        no_list.append(ans)
    else:
        print("있음")
        ok_list.append(ans)
        #중복된 모든 숫자를 찾아줘야함
        for i in range(len(word)):
            if word[i] == ans:
                word_show = word_show[:i] + ans + word_show[i+1:] #word_show 계속 없데이트

                #_ _ _ a _ n ->> _ _ c a _ n
        
        print(word_show)
    if try_num == 7: break #사람이 완성
    if word_show.find("_") == -1: break #밑줄이 없음
    

