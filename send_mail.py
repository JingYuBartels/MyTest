from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(test_report):
    sent_address = 'jingyubartels@gmail.com'
    receive_address = 'bartelsjingyu@126.com'
    body = 'Hi, there! Attachment is the latest automatin testing report. Please review!'
    username = sent_address
    password = 'Chang820124'

    with open(test_report, 'rb') as f:
        file_message = f.read()
    send_file = MIMEText(file_message, 'base64', 'uft-8')
    send_file['Content-Type'] = 'text/x-component'
    send_file['Content-Disposition'] = 'attachment; filename = test_report.html'
    msg = MIMEMultipart()
    msg['from'] = sent_address
    msg['to'] = receive_address
    msg['subject'] = 'Automation testing report'
    msg.attach(send_file)
    msg.attach(MIMEText(body, 'plain'))

    with SMTP(host='smtp.gmail.com', port=587) as server:
        server.starttls()
        server.login(username, password)
        server.send_message(msg=msg)
    print('Mail has been sent')


def new_report(TestReport_dir):
    lists = os.listdir(TestReport_dir)
    lists.sort(key=lambda x: os.path.getmtime(TestReport_dir + '/' + x), reverse=True)
    file_new = os.path.join(TestReport_dir, lists[0])
    return file_new
