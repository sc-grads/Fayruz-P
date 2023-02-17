import smtplib
from email.message import EmailMessage
from pathlib import Path

html_content = Path('test_email.html').read_text()

email = EmailMessage()
email['from'] = 'Fayruz <fayruzparuk@gmail.com>'
email['to'] = 'fayruz.paruk17@gmail.com'

email.set_content(html_content, 'html')

with smtplib.SMTP(host='smtp.office365.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login('fayruzparuk@gmail.com', 'F@yruz.1008' )
    smtp.send_message(email)
    print('The mail was sent!')