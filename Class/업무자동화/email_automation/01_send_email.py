import os
import smtplib
from email.mime.text import MIMEText
  
GOOGLE_ADD = ""
GOOGLE_PW = ""
NAVER_ADD = "clsm4569@naver.com"
NAVER_PW = ""


class EmailSender:
    email_addr = None
    password = None
    smtp_server_map = {
        'gmail.com':'smtp.gmail.com',
        'naver.com':'smtp.naver.com'
    }
    smtp_server = None

    def __init__(self, email_addr, password):
        self.email_addr = email_addr
        self.password = password
        self.smtp_server = self.smtp_server_map[email_addr.split('@')[1]]
        print(self.smtp_server)

    def send_email(self, msg, from_addr, to_addr):
        """
        :param msg: 보낼 메세지
        :param from_addr: 보내는 사람
        :param to_addr: 받는 사람
        :return:
        """
        with smtplib.SMTP(self.smtp_server, 587) as smtp:
            msg = MIMEText(msg)
            msg['From'] = from_addr
            msg['To'] = to_addr
            msg['Subject'] = "제출합니다."
            print(msg.as_string()) #string 으로 변환하여 출력

            smtp.starttls() #서버열기
            smtp.login(self.email_addr, self.password)
            smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())
            smtp.quit() #서버닫기
        print('이메일 전송이 완료 되었습니다.')

if __name__ == '__main__':

    naver_address = NAVER_ADD
    naver_password = NAVER_PW
    es_gmail = EmailSender(gmail_address, gmail_password)
    es_naver = EmailSender(naver_address, naver_password)
    es_naver.send_email('', from_addr=naver_address, to_addr="ssangyun007@naver.com")