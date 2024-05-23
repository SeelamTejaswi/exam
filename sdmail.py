import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('rathneshreddyseelam9@gmail.com','bsii kyds bevj qtog')
    msg=EmailMessage()
    msg['From']='rathneshreddyseelam9@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()