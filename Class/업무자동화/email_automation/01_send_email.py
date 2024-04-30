import os
import smtplib
from email.mime.text import MIMEText


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
            msg['Subject'] = "이메일 전송 테스트"
            print(msg.as_string())

            smtp.starttls()
            smtp.login(self.email_addr, self.password)
            smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=msg.as_string())
            smtp.quit()
        print('이메일 전송이 완료 되었습니다.')

if __name__ == '__main__':
    gmail_address = 'sy1007.lee@gmail.com'
    gmail_password = ""
    naver_address = 'ssangyun007@naver.com'
    naver_password = ""
    es_gmail = EmailSender(gmail_address, gmail_password)
    es_naver = EmailSender(naver_address, naver_password)
    es_gmail.send_email('테스트 입니다.\n구글 이메일에서 보냄', from_addr=gmail_address, to_addr=naver_address)
    es_naver.send_email('테스트 입니다.\n네이버 이메일에서 보냄', from_addr=naver_address, to_addr=gmail_address)