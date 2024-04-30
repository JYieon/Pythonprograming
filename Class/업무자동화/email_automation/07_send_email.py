import os

from libs.email_sender_with_attachment import EmailSenderWithAttachment


if __name__ == '__main__':
    gmail_address = 'sy1007.lee@gmail.com'
    gmail_password = ""

    es = EmailSenderWithAttachment(gmail_address, gmail_password,
                                   manager_name='이상윤',
                                   template_filename='templates/email_template_1.html')
    es.send_all_emails('email_list.xlsx')