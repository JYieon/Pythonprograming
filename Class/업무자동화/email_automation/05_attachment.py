import os
from libs.email_sender import EmailSender
from libs.email_sender_with_attachment import EmailSenderWithAttachment

if __name__ == '__main__':
    gmail_address = 'sy1007.lee@gmail.com'
    gmail_password = ""

    # es1 = EmailSender(gmail_address, gmail_password,
    #                  manager_name='이상윤',
    #                  template_filename='templates/email_template_1.html')
    # es1.send_all_emails('이메일리스트_with_attachment.xlsx')

    es2 = EmailSenderWithAttachment(gmail_address, gmail_password,
                     manager_name='이상윤',
                     template_filename='templates/email_template_1.html')
    es2.send_all_emails('이메일리스트_with_attachment.xlsx')