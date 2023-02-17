import smtplib
from email.message import EmailMessage
from pathlib import Path

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

html_content = Path('test_email.html').read_text()

email = MIMEMultipart()
email['from'] = 'Fayruz <fayruzparuk@gmail.com>'
email['to'] = 'fayruz.paruk17@gmail.com'

email.attach(MIMEText(html_content, 'html'))

filename = 'python.pdf'
with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment;filename={filename}')
    email.attach(part)


with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('fayruzparuk@gmail.com', 'F@yruz.1008' )
    smtp.send_message(email)
    print('The mail was sent!')