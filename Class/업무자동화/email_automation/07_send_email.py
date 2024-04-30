import os

from libs.email_sender_with_attachment import EmailSenderWithAttachment


if __name__ == '__main__':
    gmail_address = ''
    gmail_password = ""

    es = EmailSenderWithAttachment(gmail_address, gmail_password,
                                   manager_name='최지연',
                                   template_filename='templates/email_template_1.html')
    es.send_all_emails('email_list.xlsx')